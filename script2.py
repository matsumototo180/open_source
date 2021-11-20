import pandas as pd
import re
pd.set_option('display.max_rows', None)

kakei = pd.read_csv('data/pt2/アイスクリーム.csv', encoding='cp932', usecols=[2,3,5])
weather = pd.read_csv('data/pt2/気象データ.csv', encoding='cp932', skiprows=1, header=[1,2])

weather2 = weather.drop(weather.columns[0], axis=1).stack(0).reset_index(1)
weather2['月'] = weather.iloc[:,0]
weather3 = weather2.reset_index(drop=True)
weather3 = weather3.rename(columns={'level_1': '地域'})

kakei.columns = ['地域', '月', '消費金額']
kakei['消費金額'] = kakei['消費金額'].str.replace(',', '').astype(int)
kakei['地域'] = kakei['地域'].map(lambda x: re.sub(r'[0-9]+ |市|都区部', '', x))
kakei = kakei.rename(columns={'時間軸（月次）': '月'})

df = weather3.merge(kakei, how='left')

# 各都市の平均値
df.groupby('地域').mean().drop(df.columns[5], axis=1)
# 各都市の標準偏差
df.groupby('地域').std().drop(df.columns[5], axis=1)
# 各都市の月毎の平均気温と消費金額の相関係数
df.groupby('地域').apply(lambda x: x['平均気温(℃)'].corr(x['消費金額']))