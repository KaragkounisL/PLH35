with open('domains.txt', 'r') as f1:
    lines1 = f1.readlines()
with open('naunet.txt', 'r') as f2:
    lines2 = f2.readlines()
    sum = 0
for i in range(len(lines2)):
    for j in range(len(lines1)):
        if lines2[i] == lines1[j]:
            sum += 1
            print(sum, lines2[i])
print("There are %d out of %d dns query domains found on the .pcap file that are listed on the data list" % (sum, len(lines2)))
