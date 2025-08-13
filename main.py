import pandas as pd
from OSX import New_OSX

OSX = New_OSX()
print(OSX.idn)


WaveA = 850
WaveB = 1300

columns = ['ch', WaveA, WaveB, "Pass Fail"]
table = []


i = 1
while i <= num_channel:
    new_row = [i, .4, .3, 'Pass']
    table.append(new_row)
    i += 1

df = pd.DataFrame(columns=columns, data=table)
print(df)

#with pd.ExcelWriter('output.xlsx', mode='a', if_sheet_exists='replace') as writer:
#    df.to_excel(writer, sheet_name="AutoTest Measurements", index=False)
