# Simple Japanese Text Difficulty Classfication using Spacy
Repo for NLP Classfication of text difficulty using Spacy + Application with Yahoo & Wikipedia APIs.  
Personal research/learning project of mine - Ryan
## Description
This repo contains a model trained on the **I**nternational Corpus of **Ja**panese as a **S**econd Language (I-JAS) dataset found [[here]](https://chunagon.ninjal.ac.jp) [[alternative]](https://www2.ninjal.ac.jp/jll/lsaj/), a corpus of data collected from cross-sectional surveys of the spoken and written language of 1,000 Japanese learners speaking 12 different languages ​​in 20 countries and regions including Japan. Students were given two Japanese proficiency tests to determine their level; the [J-CAT](https://www.waseda.jp/inst/cjl/assets/uploads/2018/02/jcat_manual.pdf) and the [SPOT](https://ttbj.cegloc.tsukuba.ac.jp/en/p1.html#pageLink02).  

**NOTE: I can not provide the data used in the creation of this model, but it can be requested from the links above.**  

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
## Examples
Let's source some unseen texts from [TADOKU](https://tadoku.org/japanese/en/free-books-en/), a website with free online japanese texts with difficulty ratings L1 - L5.  
[[Text - L1]](https://tadoku.org/japanese/book/7348/) [[Text - L5]](https://tadoku.org/japanese/book/6238/) [[Text - IPSJ Article]](http://id.nii.ac.jp/1001/00017938/)
```
import spacy
# Genki I style sentence - Introductory
easy_text = '私は学生です。四年生です。家に、犬が一匹います。'
# Text - L1 - Medium
medium_text = '森の中に、うさぎの家族がいます。お母さんと、四匹の子うさぎです。'\
            '朝です。こどもたちは、そこであそびます。お母さんが言いました。'
# Text - L5 - Hard
hard_text = '美知子は、高校の時、広志のことが好きだった。広志はサッカー部のキャプテンでかっこよく、人気者だった。広 志の周りには、'\
            'いつもかわいい女の子が 集 まっていた。美知子は美術部だった。美術室で絵を描きながら、'\
            '校庭でボールを追いかけ走り回る広志を見ているだけでドキドキした'
# Research Article Text - Advanced
advanced_text = '「一般物体認識」とは、制約のない実世界シーンの画像に対して計算機がその中に含まれる物体を一般的な名称で認識することで、'\
                'コンピュータビジョンの究極の研究課題の1つである。人間は数万種類の対象を認識可能であるといわれるが，計算機にとっては、'\
                '同一クラスに属する対象のアピアランスが大きく変化するために以前はわずか1種類の対象を認識することすら困難であった。'

nlp = spacy.load("output/model-best")
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
### Determine the Difficulty of Current News Topics using Web Scraping:
First, the script grabs the top articles from Yahoo Japan:
```
Article #0
{'text': '来週また猛烈な暑さか 体温超えも', 'url': 'https://news.yahoo.co.jp/pickup/6470100', 'ents': ''}
Article #1
{'text': 'ウ大統領 クリミア橋攻撃を示唆', 'url': 'https://news.yahoo.co.jp/pickup/6470104', 'ents': 'ウ 大統領 クリミア橋攻撃'}
Article #2
{'text': '3児溺れ死亡 泣いて眠れない子も', 'url': 'https://news.yahoo.co.jp/pickup/6470107', 'ents': '3児'}
Article #3
{'text': '女性殴られ死亡 傷害疑いで女逮捕', 'url': 'https://news.yahoo.co.jp/pickup/6470109', 'ents': ''}
Article #4
{'text': '「最悪の侵略的植物」 千葉で苦悩', 'url': 'https://news.yahoo.co.jp/pickup/6470106', 'ents': '最悪の侵略的植物 千葉'}
Article #5
{'text': '井上尚弥に相手陣営が「神経戦」', 'url': 'https://news.yahoo.co.jp/pickup/6470087', 'ents': '井上'}
Article #6
{'text': 'ロコ・藤沢五月 ムキムキ姿を披露', 'url': 'https://news.yahoo.co.jp/pickup/6470105', 'ents': ''}
Article #7
{'text': 'まずい 欽ちゃん語る脳梗塞の経験', 'url': 'https://news.yahoo.co.jp/pickup/6470108', 'ents': '欽ちゃん'}
Select an article to search:
5
```
We then search wikipedia for any relevant topics recognized by the model:
```
Wiki Page #0
井上
Wiki Page #1
井上馨
Wiki Page #2
井上ひさし
Wiki Page #3
井上順
Wiki Page #4
井上大輔
Wiki Page #5
井上咲楽
Wiki Page #6
井上毅
Wiki Page #7
井上八千代
Wiki Page #8
井上内親王
Wiki Page #9
井上堯之
```
Since none of these articles relate to the actual article, you can also enter in your own prompt:
```
Select a wikipedia page to categorize (-1 for your own search):
-1
Enter in your search prompt:
井上尚弥
井上 尚弥（いのうえ なおや、1993年〈平成5年〉4月10日）は、日本のプロボクサー。神奈川県座間市出身。大橋ボクシングジム所属。元WBC世界ライトフライ級王者。元WBO世界スーパーフライ級王者。元WBAスーパー・WBC・IBF・WBOスーパー世界バンタム級統一王者。世界3階級制覇王者。WBSSバンタム級王者。史上9人目、アジア人初の主要4団体統一王者。
圧倒的実力と完璧なボクシングスタイルから『日本ボクシング史上最高傑作』と呼ばれており、世界で最も権威のあるアメリカのボクシング専門誌「ザ・リング」が格付けするパウンド・フォー・パウンドランキングにおいて、日本人として史上初めて1位の評価を受けた。アマチュア時代には日本ボクシング史上初めて高校生にして7つのタイトルを獲得し、プロ転向後も8戦目での2階級制覇、世界王座戦19連勝、世界王座戦17KO勝利、世界王座戦70秒での最短KO勝利、世界王座海外防衛4度など数多くの日本記録を樹立している。
血液型A型。既婚。三児の父親。弟は元WBC世界バンタム級暫定王者、現WBA世界バンタム級王者の井上拓真。姉もいる。従兄にプロボクサーの井上浩樹。父親の井上真吾は元アマチュアボクサーの実業家で、大橋ボクシングジム所属のプロボクシングトレーナーとして2人の我が子と甥である浩樹の担当トレーナーも務めている。
{'easy': 0.012185882776975632, 'medium': 0.5864529013633728, 'advanced': 0.4490154981613159}
```
## References
K. Sakoda (2020). I-JAS tanjo no keii. [The background of compilation of I-JAS]. In K. Sakoda, S. Ishikawa, & J. Lee (Eds.), Nihongo gakushusha kopasu I-JAS nyumon: Kenkyu kyoiku ni do tsukauka [Introduction to the I-JAS: Application for research and teaching](pp. 2-13).Kurosio Publishers
