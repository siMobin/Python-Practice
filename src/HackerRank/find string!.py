n = int(input())
z = []
for x in range(n):
    x = input()
    z.append(x)

for i in z:
    try:
        if i.find(".") != -1:
            i = float(i)
        else:
            i = int(i)
    except:
        pass
    finally:
        # print(type(i))
        if type(i) == str or i == 0:  # 0!?
            print(False)
        else:
            print(True)
