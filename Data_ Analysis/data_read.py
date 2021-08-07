in_file = open('test1.txt', 'r', encoding='utf-8')

for i in in_file:
    print(i.strip())
in_file.close()
