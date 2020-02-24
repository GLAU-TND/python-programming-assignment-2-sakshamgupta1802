given_list = eval(input())
output_list = []
for i in given_list:
    last = i[-1]
    for j in given_list:
        if j[0] == last:
            output_list.append(i)
            output_list.append(j)
            given_list.remove(i)
            given_list.remove(j)
print(output_list+given_list)