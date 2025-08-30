
try:
    file=open('Sample.txt', 'r')
    print('Line 1:',file.readline())
    print('Line 2:',file.readline())
    file.close()
except FileNotFoundError:
    print('Error:The file \'Sample.txt\' was not found.')





