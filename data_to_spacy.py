import pandas as pd
from sklearn.model_selection import train_test_split
from spacy.tokens import DocBin
import spacy


def make_docs(data):
    docs = []
    for doc, label in nlp.pipe(data, as_tuples=True):
        if label > float(0.689):
            doc.cats['easy'] = 0
            doc.cats['medium'] = 0
            doc.cats['advanced'] = 1
        elif label < float(0.464):
            doc.cats['easy'] = 1
            doc.cats['medium'] = 0
            doc.cats['advanced'] = 0
        elif float(0.689) >= label >= float(0.464):
            doc.cats['easy'] = 0
            doc.cats['medium'] = 1
            doc.cats['advanced'] = 0
        # print(label, doc.cats)
        docs.append(doc)
    return docs


df = pd.read_excel('./data/raw_data.xlsx')

train, test = train_test_split(df, test_size=0.33)  # Can change random_state for set outcomes
print('Training Data Shape:', train.shape)
print('Testing Data Shape:', test.shape)

train_data = list(zip(train['Text'], train['Difficulty']))
test_data = list(zip(test['Text'], test['Difficulty']))
full_data = list(zip(df['Text'], df['Difficulty']))

# Load pre-trained model
nlp = spacy.load("ja_core_news_lg")

train_docs = make_docs(train_data)
doc_bin = DocBin(docs=train_docs)
doc_bin.to_disk('./data/train.spacy')

test_docs = make_docs(test_data)
doc_bin = DocBin(docs=test_docs)
doc_bin.to_disk('./data/test.spacy')

# full_docs = make_docs(full_data)
# doc_bin = DocBin(docs=full_docs)
# doc_bin.to_disk('./data/full.spacy')
