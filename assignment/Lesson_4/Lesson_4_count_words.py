# count all unique words in any text with ,:? etc
result = {}
file = open('data.txt', 'r')
for line in file.readlines():
    for word in line.split():
        word = ''.join([x for x in word if x.isalnum()])
        result[word] = result.setdefault(word, 0) + 1
file.close()
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(sorted_result)