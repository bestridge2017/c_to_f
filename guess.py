import random

r = random.randint(1,100)

while True:
    g = input('请输入您猜想的数字：')
    g = int(g)
    if g == r:
        print('恭喜您，您猜对了')
        break
    elif g > r: 
    	print('比答案大')
    elif g < r:
        print('比答案小')

    