# diff-classification_ja
Repo for NLP Classfication of text difficulty using Spacy. Personal research/learning project of mine - Ryan
## Description
This repo contains a model trained on the **I**nternational Corpus of **Ja**panese as a **S**econd Language (I-JAS) dataset found [[here]](https://chunagon.ninjal.ac.jp) [[alternative]](https://www2.ninjal.ac.jp/jll/lsaj/), a corpus of data collected from cross-sectional surveys of the spoken and written language of 1,000 Japanese learners speaking 12 different languages ​​in 20 countries and regions including Japan. Students were given two Japanese proficiency tests to determine their level; the J-CAT and the SPOT.
## Limitations
This model is limited by amount of data, as well as the classification of data into difficulty levels. I based my classification of difficulty on quantitative scores of the J-CAT and SPOT, but these scores are not fully representative of the proficiency a learner is at. 
## Usage
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
