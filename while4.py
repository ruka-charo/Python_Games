#while３で操作を一度に任意の範囲の数に対し行う

#要素の追加(任意の領域)
a = input('調べたい自然数の下限を入力してください。:')
a = int(a)

n = a
n_s = [n]

N = input('調べたい自然数の上限を入力してください。:')
N = int(N)

while n <= N :
    n = n + 1
    n_s.append(n)
    if n == N :
        break

#リスト内の数字に全てについて操作を行う
for x in n_s :
    print(x)

    while x >=5 :

        if x % 2 == 0 :
            x = x - 1

        elif x % 3 == 0 :
            x = x - 2

        elif x % 5 == 0 :
            x = x - 2

        elif x % 5 == 2 :
            x = x - 4

        else :
            x = x - 3

    print(x)
