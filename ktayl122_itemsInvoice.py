items = int(input("Number of items: "))
list=dict()
for i in range(items):
    itemInput = input(("Input item and price: "))
    temp = itemInput.split(' ')
    list[temp[0]] = int(temp[1])
    sort_list=sorted(list.items(), key=lambda x : x[1])
    for i in sort_list:
        print(i[0], i[1])