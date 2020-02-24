given_binary = list(bin(int(input())))
new = []
for i in range(0, len(given_binary)):
    c = 0
    if given_binary[i] == '1':
        for j in range(i, len(given_binary)):
            if given_binary[j] == '1':
                c += 1
            else:
                break
        new.append(c)
print(max(new))
