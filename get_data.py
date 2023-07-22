import openpyxl
import os
import re
import pandas as pd

wb = openpyxl.load_workbook('./data/jpn_data_scored.xlsx')
sheet = wb['jpn_data']

data = []

for r in sheet.rows:
    lang = r[0].value[0:3]
    id_num = r[0].value[3:5]
    score = r[8].value
    # print(lang, id_num, level)
    for root, dirs, files in os.walk(f'./data/file_repo/{lang}'):
        for name in files:
            if id_num in name:
                text_arr = []
                with open(os.path.join(root, name), encoding="utf8", mode='r') as f:
                    line = f.readline()  # include newline
                    while line:
                        line = re.sub(r'[A-Z]{3}[0-9]{2}-[A-Z0-9]{1,3}-[0-9]{3,}-[A-Z]', '', line)  # Cleanup text file
                        line = line.rstrip().strip()  # strip trailing spaces and newline
                        # process the line
                        text_arr.append(line)
                        line = f.readline()
                text = '、 '.join(text_arr)
                data.append([text, score])

df = pd.DataFrame(data, columns=['Text', 'Difficulty'])
df.to_excel('./data/raw_data.xlsx')
