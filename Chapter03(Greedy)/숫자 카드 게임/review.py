n, m = map(int,input().split())

result=0

for i in range(n):
    my_data=list(map(int,input().split()))
    
    min_value=min(my_data)

    result = max(result,min_value)

print("result: ",result)