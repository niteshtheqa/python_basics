with open('./README.md', 'r') as f:

    for line in f:
        print(line, end='')
        print("Length of file:  ",len(line))


