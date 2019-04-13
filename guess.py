import random
start = input('请决定随机数字开始值：')
end = input('请决定随机数字范围结束值：')
start = int(start)
end = int(end)

r = random.randint(start,end)

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

    