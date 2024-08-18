def my_insert(origin, ins):

    pass
def my_del(origin, d):
    pass

len_password = int(input())
origin_password = list(map(int, input().split()))
count_command = int(input())
command = list(input().split())
ins = []
d = []
for i in range(len(command)):
    if command[i] == 'I':
        ins.append(command[i+1])
        ins.append(command[i+2])
        for idx in range(1, int(command[i+2]) + 1):
            ins.append(command[i+2+idx])
    elif command[i] == 'D':
        d.append(command[i+1])
        d.append(command[i+2])


