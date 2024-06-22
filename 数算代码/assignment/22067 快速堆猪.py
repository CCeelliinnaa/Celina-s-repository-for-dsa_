pig=[]
while True:
    try:
        x=input()
        if x=='min' and pig:
            print(pig[-1])
        elif x=='pop' and pig:
            pig.pop()
        elif x[-1].isdigit():
            weight=int(x.split()[1])
            if not pig:
                pig.append(weight)
            pig.append(min(pig[-1],weight))###太妙了，看什么时候最小值会被赶走。
    except EOFError:
        break