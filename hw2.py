import random


def is_not_exit(list1, num):
    for i in range(0, len(list1), 1):
        if list1[i] == num:
            return False

    return True


count = 6
inputs = []

while True:
    num = int( input('1~45 사이의 번호 입력 : ') )

    if num < 1 or num > 45:
        print('1~45사이의 번호를 입력해야 합니다....')
    else:
        if is_not_exit(inputs, num):
            inputs.append(num)
            
            if len(inputs) >= count:
                break
        else:
            print('이미 입력한 번호입니다...')

lottos = []

while True:
    rnum = random.randint(1, 45)

    if is_not_exit(lottos, rnum):
        lottos.append( rnum )

        if len(lottos) >= count:
            break
    else:
        continue

print('이번주 번호 : ', lottos)
print('당신의 번호 : ', inputs)

corrects = []
perfect = True

for x in range(0, count, 1):
    existed = False
    
    for y in range(0, count, 1):
        if inputs[x] == lottos[y]:
            corrects.append(inputs[x])
            existed = True
            break

    if not existed:
        perfect = False

if perfect:
    print('당첨')
else:
    print('맞은 번호 : ', corrects)
    print('다음기회에....')
