N = input()
file = []
for i in range(int(N)):
    file_line = input().split(' ')
    file.append(file_line)
error = []
for k in range(int(N)):
    if (file[k][1] == 'false'):
        error.append(file[k][2])
if (len(error) == 0):
    print('Yes')
    print(error)
else:
    print('No')
    print(*error, sep=' ')
