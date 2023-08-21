n=int(input("map size:"))
m=list(input("movement: ").split())
start=[1,1]

my_mov={"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}

for i in m:
    if i=="L":
        if start[1]==1:
            continue
        else:
            start[1]+=my_mov["L"][1]
    elif i=="R":
        if start[1]==n:
            continue
        else:
            start[1]+=my_mov["R"][1]
    elif i=="U":
        if start[0]==1:
            continue
        else:
            start[0]+=my_mov["U"][0]
    elif i=="D":
        if start[0]==n:
            continue
        else:
            start[0]+=my_mov["D"][0]

print("coordinate: ", start)