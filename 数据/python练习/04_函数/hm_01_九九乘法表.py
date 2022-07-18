def multiple_table():
    row = int(input("输入想要输出乘法表（10以内）星号："))
    sum = 0
    while row <=9 :
        col = 1
        while col <= row :
            sum = row * col
            print("%d * %d = %d" % (row,col,sum),end=" \t")
            col += 1
        row +=1
        print ("")