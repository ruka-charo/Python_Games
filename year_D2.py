#年号から西暦に変換

nengo = int(input('元号を入力してください。（令和：1、平成：2、昭和：3、大正：4）:'))
number = int(input('「年」を入力してください。:'))

if nengo == 1 :
    year = 2019 + number - 1
    print('令和' + str(number) + '年は、西暦' + str(year) + '年です。')

elif nengo == 2 :
    year = 1989 + number - 1
    print('平成' + str(number) + '年は、西暦' + str(year) + '年です。')

elif nengo == 3 :
    year = 1926 + number - 1
    print('昭和' + str(number) + '年は、西暦' + str(year) + '年です。')

else :
    year = 1912 + number - 1
    print('大正' + str(number) + '年は、西暦' + str(year) + '年です。')
