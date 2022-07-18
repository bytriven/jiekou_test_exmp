def print_line(char,times) :
    print(char * times)
def print_lines(char,times) :
    row = 0
    while row < 5:
        print_line(char,times)
        row +=1
print_lines(str(input("输入分割线字符：")),int(input("输入打印次数：")))