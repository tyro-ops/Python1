number = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0

for val in number:
    sum = sum+val
# print(sum)


genre = ['bhh', 'pop', 'jazz']

for i in genre:
    # ange(len(genre)):
    print(i.find('pop'))
    if i.find('pop'):
        print(i)
    else:
        print("Not found")


genre = ['rock', 'pop', 'jazz']


print(list(range(10)))
print(list(range(2, 8)))


genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for j in range(len(genre)):
    print("I like", genre[j])
