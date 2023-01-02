# algorithm 1
def sorter0(line):
    my_list = []
    count = 65
    while len(my_list) < len(line):
        for i in line:
            print(f"i is {i}")
            if ord(i) == count:
                my_list.append(i)
                count += 1
    print(f"list is {my_list}")

#algorithm 2
def sorter(line):
    my_list = []

    aicc = map(ord, line)
    aicc = list(aicc)

    i = 0
    while i < len(line):
        lowest = min(aicc)

        ch = chr(lowest)
        my_list += ch
        aicc.remove(lowest)

        i += 1

    print(my_list)

sorter('fjtidvnghritjh')
