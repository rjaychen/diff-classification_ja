# Simple Japanese Text Difficulty Classfication using Spacy
Repo for NLP Classfication of text difficulty using Spacy + Application with Yahoo & Wikipedia APIs.  
Personal research/learning project of mine - Ryan
## Description
This repo contains a model trained on the **I**nternational Corpus of **Ja**panese as a **S**econd Language (I-JAS) dataset found [[here]](https://chunagon.ninjal.ac.jp) [[alternative]](https://www2.ninjal.ac.jp/jll/lsaj/), a corpus of data collected from cross-sectional surveys of the spoken and written language of 1,000 Japanese learners speaking 12 different languages ​​in 20 countries and regions including Japan. Students were given two Japanese proficiency tests to determine their level; the [J-CAT](https://www.waseda.jp/inst/cjl/assets/uploads/2018/02/jcat_manual.pdf) and the [SPOT](https://ttbj.cegloc.tsukuba.ac.jp/en/p1.html#pageLink02).  
## Limitations
This model is limited by amount of data (n<10000), as well as the classification of data into difficulty levels. I based my classification of difficulty on quantitative scores of the J-CAT and SPOT, but these scores are not fully representative of the proficiency a learner is at.  
  
Due to the limited amount of data, I opted to use **k-fold cross validation** with a k = 4 segmentation. The k-fold program is taken from [here](https://github.com/explosion/projects/blob/v3/tutorials/parser_low_resource/scripts/kfold.py)
## Evaluation
The output of training with a learning rate of .001:
```
E    #       LOSS TEXTC...  CATS_SCORE  SCORE
---  ------  -------------  ----------  ------
  0       0           0.25       50.05    0.50
  0     200          43.31       52.94    0.53
  0     400          36.12       58.68    0.59
  0     600          37.58       59.37    0.59
  0     800          37.61       59.33    0.59
  0    1000          36.52       60.98    0.61
  1    1200          27.41       64.07    0.64
  1    1400          26.11       64.83    0.65
  1    1600          26.99       63.78    0.64
  1    1800          26.51       66.35    0.66
  1    2000          24.00       62.95    0.63
  2    2200          20.85       68.45    0.68
  2    2400          18.38       66.58    0.67
  2    2600          17.14       70.22    0.70
  2    2800          16.21       66.73    0.67
  2    3000          22.74       65.70    0.66

```
## Usage
### Training the Model
You can download the spacy model used in training my model through the following steps:
1. Install spacy
```
pip install spacy
```
2. Install the model
```
python -m spacy download "ja_core_news_lg"
```
A requirements.txt is also provided for package installation. 
### Web Scraping
## Examples

