'''range (0,22);
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print(x, y, z)
'''
'''from random import randint
money = int(1000)
while money > 0:
       print('你的总资产为:', money)
       needs_go_on = False
       while True:
           debt = int(input('请下注: '))
           if 0 < debt <= money:
               break
       first = randint(1, 6) + randint(1, 6)
       print('玩家摇出了%d点' % first)
       if first == 7 or first == 11:
           print('玩家胜!')
           money += debt
       elif first == 2 or first == 3 or first == 12:
           print('庄家胜!')
           money -= debt
       else:
           needs_go_on = True
       while needs_go_on:
           needs_go_on = False
           current = randint(1, 6) + randint(1, 6)
           print('玩家摇出了%d点' % current)
           if current == 7:
               print('庄家胜')
               money -= debt
           elif current == first:
               print('玩家胜')
               money += debt
           else:
               needs_go_on '''

m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)
