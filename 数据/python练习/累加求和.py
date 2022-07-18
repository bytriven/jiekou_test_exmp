number = int(input("输入开始累加的数字："))
sum = 0
if number < 100 :
    while number < 100 :
        sum += number
        print("输出数字是： %d ,输出的求和结果是： %d " % (number,sum))
        number += 1
else :
    print("你输入的数过大，请输入100以内的数字,下面是对大于100且小于1000的偶数进行相加")
    print("↓(ಥ﹏ಥ)" * 10)
    if number <= 1000 :
        while number <= 1000 :
            if number % 2 == 0 :
                sum += number
                print("输出数字是： %d ,输出的求和结果是： %d " % (number,sum))
            number += 1
    else :
        print("你输入的数字过大。为 %d ,我计算不过来。" % number)