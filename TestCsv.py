import csv
with open('MI_5MINS_HIST.csv', encoding='big5') as f:
    rows = []
    for row in list(csv.reader(f))[1:]:
        rows.append(row)
        print(row[0], row[4], sep='\t')
    # import pandas as pd
    # print(pd.DataFrame(rows))


