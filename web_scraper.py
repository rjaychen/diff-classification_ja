from bs4 import BeautifulSoup
import requests
import wikipedia
import spacy

url = 'https://yahoo.co.jp'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html5lib')

titles = []

# Grab Topics from Yahoo
topics = soup.find('section', attrs={'id': 'tabpanelTopics1'})

for row in topics.find_all('article', attrs={'class': 'QLtbNZwO-lssuRUcWewbd'}):
    title = {'text': row.find('span', attrs={'class': 'fQMqQTGJTbIMxjQwZA2zk'}).text,
             'url': row.a['href'],
             'ents': ''}
    titles.append(title)

# Extract Relevant Information using Spacy NER
nlp = spacy.load('ja_core_news_lg')

for title in titles:
    doc = nlp(title['text'])
    for ent in doc.ents:
        title['ents'] = ' '.join([title['ents'], ent.text])
        # print(ent.text, ent.label_)
    title['ents'] = title['ents'].strip()
# Search News in Wikipedia
wikipedia.set_lang('ja')
for i in range(len(titles)):
    print(f'Article #{i}')
    print(titles[i])
title_id = int(input("Select an article to search:\n"))

if titles[title_id]['ents']:
    search = wikipedia.search(titles[title_id]['ents'])
    for i in range(len(search)):
        print(f'Wiki Page #{i}')
        print(search[i])
    page_id = input("Select a wikipedia page to categorize (-1 for your own search):\n")
    page_id = int(page_id) if not '-1' else input("Enter in your search prompt:\n")
    if type(page_id) == int:
        page = wikipedia.page(search[page_id])
    else:
        page = wikipedia.page(page_id)
    print(page.summary)
    nlp = spacy.load("output/model-best")
    page_doc = nlp(page.summary)
    print(page_doc.cats)
else:
    print('The article chosen has no recognizable entities.')
