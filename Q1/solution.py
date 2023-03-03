N = input()
tshirts_str = input().split(' ')

M = input()
requests_str = input().split(' ')

tshirts = []
for t in tshirts_str:
    if t == 'S':
        tshirts.append(1)
    elif t == 'M':
        tshirts.append(2)
    elif t == 'L':
        tshirts.append(3)
    else:
        x_cnt = 0
        for x in t:
            if x == 'X':
                x_cnt += 1
            else:
                if x == 'L':
                   tshirts.append(3 * 10 ** x_cnt) 
                else:
                    tshirts.append(1 / (10 ** x_cnt))
tshirts.sort()

requests = []
for t in requests_str:
    if t == 'S':
        requests.append(1)
    elif t == 'M':
        requests.append(2)
    elif t == 'L':
        requests.append(3)
    else:
        x_cnt = 0
        for x in t:
            if x == 'X':
                x_cnt += 1
            else:
                if x == 'L':
                   requests.append(3 * 10 ** x_cnt) 
                else:
                    requests.append(1 / (10 ** x_cnt))
requests.sort()

t_index = 0
r_index = 0
complete = 0

while (r_index < len(requests)):
    if (requests[r_index] <= tshirts[t_index]):
        complete += 1
        r_index += 1
        t_index +=1
    else:
        t_index += 1
if (complete == len(requests)):
    print("Yes")
else:
    print("No")
