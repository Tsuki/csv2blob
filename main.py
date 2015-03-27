import csv

with open('template.csv', 'rb') as csvSrc:
    bufferReader = csv.reader(csvSrc, delimiter=',')
    bufferWriter = csv.writer(open('complete.csv', 'wb'), delimiter=',')
    bufferWriter.writerow(['template','blob code'])
    for line in bufferReader:
        line.insert(1, "")
        for c in line[0]:
            line[1] += format(ord(c), 'x')
        line[1]='0x'+line[1]
        bufferWriter.writerow(line)
