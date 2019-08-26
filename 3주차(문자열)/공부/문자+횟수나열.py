data = 'aabbccaa'
result = ''

cnt = 1
for i in range(1, len(data)):
    if data[i] == data[i-1]:
        cnt += 1
    else:
        result += data[i-1] + str(cnt)
        cnt = 1
    
    if i == len(data) - 1:
        result += data[i] + str(cnt)

print(result)