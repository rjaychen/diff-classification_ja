# Simple Japanese Text Difficulty Classfication using Spacy
Repo for NLP Classfication of text difficulty using Spacy + Application with Yahoo & Wikipedia APIs.  
Personal research/learning project of mine - Ryan
## Description
This repo contains a model trained on the **I**nternational Corpus of **Ja**panese as a **S**econd Language (I-JAS) dataset found [[here]](https://chunagon.ninjal.ac.jp) [[alternative]](https://www2.ninjal.ac.jp/jll/lsaj/), a corpus of data collected from cross-sectional surveys of the spoken and written language of 1,000 Japanese learners speaking 12 different languages ​​in 20 countries and regions including Japan. Students were given two Japanese proficiency tests to determine their level; the [J-CAT](https://www.waseda.jp/inst/cjl/assets/uploads/2018/02/jcat_manual.pdf) and the [SPOT](https://ttbj.cegloc.tsukuba.ac.jp/en/p1.html#pageLink02).  

I used a similar pipeline as the ja_core_news_lg model, using the "tok2vec","morphologizer","parser", and "ner" components as annotations for categorization. 
## Limitations
This model is limited by amount of data (n<10000), as well as the classification of data into difficulty levels. I based my classification of difficulty on quantitative scores of the J-CAT and SPOT, but these scores are not fully representative of the proficiency a learner is at. Furthermore, there is a large disparity in the number of advanced, intermediate, and beginner/introductory learners in the data set.
  
Due to the limited amount of data, I opted to use **k-fold cross validation** with a k = 5 segmentation, instead of a train/test split. The k-fold program is modified from [here](https://github.com/explosion/projects/blob/v3/tutorials/parser_low_resource/scripts/kfold.py)
## Evaluation
The output of training with a learning rate of .001 using train/div:
```
E    #       LOSS TEXTC...  CATS_SCORE  SCORE
---  ------  -------------  ----------  ------
  0       0           0.05   49.52    0.87
  0     200          42.16   50.43    0.87
  0     400          33.78   56.67    0.89
  0     600          36.91   59.44    0.89
  0     800          29.90   64.05    0.91
  0    1000          31.22   68.31    0.92
  1    1200          27.70   65.82    0.91
  1    1400          31.31   67.71    0.92
  1    1600          27.88   73.76    0.93
  1    1800          29.96   69.49    0.92
  1    2000          30.78   70.37    0.92
  2    2200          23.02   70.73    0.92
  2    2400          26.00   65.17    0.91
  2    2600          25.82   77.96    0.94
  2    2800          23.36   65.43    0.91
  2    3000          24.24   68.22    0.92
  3    3200          25.76   78.05    0.94
  3    3400          21.75   75.37    0.94
  3    3600          18.61   78.24    0.94
  3    3800          18.99   76.99    0.94
  4    4000          18.33   79.65    0.95
  4    4200          16.54   79.94    0.95
  4    4400          14.57   80.22    0.95
  4    4600          16.93   80.69    0.95
  5    4800          10.22   78.42    0.94
  5    5000          14.31   79.35    0.95
  5    5200          11.03   77.99    0.94
  6    5400           6.28   76.34    0.94
  6    5600           7.63   76.96    0.94
  7    5800           7.03   75.99    0.94
  7    6000           3.08   74.99    0.93
  7    6200           5.74   78.31    0.94
```
The output of training with k-folds:
## Usage
### Training the Model
You can download the spacy model used in training my model through the following steps (A requirements.txt is also provided for package installation):
1. Install spacy
```
pip install spacy
```
2. Install the model
```
python -m spacy download "ja_core_news_lg"
``` 
3. Train the model
```
python -m spacy train config.cfg --output ./output
```
Use either the train.py module to produce .spacy DocBin files for training purposes, or alternatively, run the k-fold algorithm.
### Web Scraping
## Examples
Let's source some unseen texts from [TADOKU](https://tadoku.org/japanese/en/free-books-en/), a website with free online japanese texts with difficulty ratings L1 - L5.  
[[Text - L1]](https://tadoku.org/japanese/book/7348/) [[Text - L5]](https://tadoku.org/japanese/book/6238/) [[Text - IPSJ Article]](http://id.nii.ac.jp/1001/00017938/)
```
import spacy
# Genki I style sentence
easy_text = '私は学生です。四年生です。家に、犬が一匹います。'
# Text - L1
medium_text = '森の中に、うさぎの家族がいます。お母さんと、四匹の子うさぎです。'\
            '朝です。こどもたちは、そこであそびます。お母さんが言いました。'
# Text - L5
hard_text = '美知子は、高校の時、広志のことが好きだった。広志はサッカー部のキャプテンでかっこよく、人気者だった。広 志の周りには、'\
            'いつもかわいい女の子が 集 まっていた。美知子は美術部だった。美術室で絵を描きながら、'\
            '校庭でボールを追いかけ走り回る広志を見ているだけでドキドキした'
# Research Article Text
advanced_text = '「一般物体認識」とは、制約のない実世界シーンの画像に対して計算機がその中に含まれる物体を一般的な名称で認識することで、'\
                'コンピュータビジョンの究極の研究課題の1つである。人間は数万種類の対象を認識可能であるといわれるが，計算機にとっては、'\
                '同一クラスに属する対象のアピアランスが大きく変化するために以前はわずか1種類の対象を認識することすら困難であった。'

nlp = spacy.load("output/model-best")
easy_doc = nlp(easy_text)
medium_doc = nlp(medium_text)
hard_doc = nlp(hard_text)
advanced_doc = nlp(advanced_text)
print('Introductory:')
print(easy_doc.cats)
print('Medium:')
print(medium_doc.cats)
print('Hard:')
print(hard_doc.cats)
print('Advanced:')
print(advanced_doc.cats)
```
Output:
```
Introductory:
{'easy': 0.7296032309532166, 'medium': 0.1260347068309784, 'advanced': 0.14535404741764069}
Medium:
{'easy': 0.027298055589199066, 'medium': 0.6981500387191772, 'advanced': 0.19801360368728638}
Hard:
{'easy': 0.045824140310287476, 'medium': 0.39197373390197754, 'advanced': 0.502650797367096}
Advanced:
{'easy': 0.01567140780389309, 'medium': 0.23157335817813873, 'advanced': 0.7423866391181946}
```
