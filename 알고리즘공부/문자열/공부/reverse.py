s = 'Reverse ths strings'
sr =''

for i in range(len(s)-1, -1, -1):
    sr += s[i]

print(sr)