while True:
    x = int(input())
    if x != 0 and x <= 1000 and x >= -1000:
        break
while True:
    y = int(input())
    if y != 0 and y <= 1000 and y >= -1000:
        break

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")  
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")