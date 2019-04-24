# utf-8
import pandas as pd
import glob, os

file_path = '..\\csv_path'
csvs = os.listdir(file_path)

results = pd.DataFrame([])
for counter, file in enumerate(csvs):
    # csv_path = open(os.path.join(file_path, file), encoding='utf-8-sig')
    csv_path = open(os.path.join(file_path, file))
    df_temp = pd.read_csv(csv_path)
    results = results.append(df_temp, ignore_index=True)

print(results)
results.to_csv('..\\new_file.csv', index=0, encoding='utf-8')
print('csv saved ok ......')

