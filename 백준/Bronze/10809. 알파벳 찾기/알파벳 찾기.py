s = input().lower()
a = 'abcdefghijklmnopqrstuvwxyz'
for i in a :
    if i in s:
        print(s.index(i), end= ' ')
    else :
        print(-1, end=' ')