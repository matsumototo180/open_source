import csv
import pprint
last_name = ['佐藤', '鈴木', '高橋', '田中', '伊藤', '渡辺', '山本',
             '中村', '小林', '加藤', '吉田', '山田', '佐々木', '山口', '井上']
first_name = ['太郎', '浩', '裕子', '二郎', '由美', '恵子', '健一',
              '美香', '恵', '里奈', '健太郎', '拓哉', '春香', '直樹', '美由紀']
sex = ['男', '男', '女', '男', '女', '女', '男',
       '女', '女', '女', '男', '男', '女', '男', '女']

kokugo_score = [63, 74, 45, 85, 55, 58, 70, 83, 90, 83, 42, 80, 75, 70, 67]
sugaku_score = [53, 84, 70, 65, 83, 66, 50, 77, 69, 50, 64, 80, 64, 53, 69]
eigo_score = [80, 72, 57, 70, 62, 73, 72, 75, 92, 73, 54, 72, 78, 58, 70]

dict_list = []
for lname, fname, sex, kokugo, sugaku, eigo in zip(last_name, first_name, sex, kokugo_score, sugaku_score, eigo_score):
    dict_list.append(
        {'氏名': ' '.join([lname, fname]),
         '性別': sex,
         '国語': kokugo,
         '数学': sugaku,
         '英語': eigo,
         '合計': kokugo + sugaku + eigo
         }
    )

score_male = []
score_female = []
for item in dict_list:
    if item['性別'] == '男':
        score_male.append(item['合計'])
    else:
        score_female.append(item['合計'])

num_of_class = len(last_name)

avg_class = sum([i['合計'] for i in dict_list]) / num_of_class
avg_male = sum(score_male) / len(score_male)
avg_female = sum(score_female) / len(score_female)

print(f'クラスの平均点:\t{avg_class}\n男子の平均点:\t{avg_male}\n女子の平均点:\t{avg_female}')

with open('output.csv', 'w', newline="") as f:
    writer = csv.DictWriter(f, fieldnames=dict_list[0].keys())
    writer.writeheader()
    writer.writerows(dict_list)
