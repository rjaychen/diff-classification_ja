import spacy

easy_text = '私は学生です。四年生です。家に、犬が一匹います。'

medium_text = '森の中に、うさぎの家族がいます。お母さんと、四匹の子うさぎです。'\
            '朝です。こどもたちは、そこであそびます。お母さんが言いました。'

hard_text = '美知子は、高校の時、広志のことが好きだった。広志はサッカー部のキャプテンでかっこよく、人気者だった。広 志の周りには、'\
            'いつもかわいい女の子が 集 まっていた。美知子は美術部だった。美術室で絵を描きながら、'\
            '校庭でボールを追いかけ走り回る広志を見ているだけでドキドキした'

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
