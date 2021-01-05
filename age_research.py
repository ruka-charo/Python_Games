#誕生日から現在の年齢を計算する。
import datetime

today = datetime.date.today()

y = int(input('誕生年を入力してください。:'))
m = int(input('誕生月を入力してください。:'))
d = int(input('誕生日を入力してください。:'))
birthday = datetime.date(y,m,d)

day = today - birthday

age = day.days // 365

print('今日の日付は' + str(today) + 'です。')
print('入力された誕生日は' + str(y) + '年' + str(m) + '月' + str(d) + '日です。')
print('現在の年齢を計算します。')
print('年齢は' + str(age) + '才です。')
