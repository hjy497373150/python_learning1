fp = open('record.txt', 'r+')
for each_line in fp:
    print(each_line)
fp.write("hello java")
fp.close()


