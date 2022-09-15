from collections import Counter
firstdict = {'a': 75, 'b': 284, 'c': 312}
seconddict = {'a': 11, 'b': 582, 'd': 445}
solution = Counter(firstdict) + Counter(seconddict)
print(solution)