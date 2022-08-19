import csv
with open('MI_5MINS_HIST.csv', encoding='big5') as f:
    print('日期\t\t收盤指數')
    for row in csv.DictReader(list(f)[1:]):
        print(row['日期'], row['收盤指數'], sep='\t')
        
    # print(list(csv.DictReader(list(f)[1:])))
    # import pandas as pd
    # print(pd.DataFrame(csv.DictReader(list(f)[1:])))



