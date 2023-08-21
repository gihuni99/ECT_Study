my_coo=input("coordinate: ")

movement=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
count=0

for move in movement:

    row=int(my_coo[1])
    col=int(ord(my_coo[0])-ord('a')+1)

    row+=move[0]
    col+=move[1]

    if row<=0 or row>8 or col<=0 or col>8:
        continue
    else:
        count+=1

print("result: ",count)