inp = str(input())
rev = ""
i = len(inp) - 1
while i >= 0:
    rev = rev + inp[i]
    i = i - 1

print(rev)