from asyncio.windows_events import NULL


l =[9, -3, -1, 2, -4] 

i = 0
numbers = len(l)
result = NULL

while i < numbers:
    result = result +l[i]
    print(l[i])
    i += 1 # i = i+1

print(result)

#x = sum(l)
#print(x)