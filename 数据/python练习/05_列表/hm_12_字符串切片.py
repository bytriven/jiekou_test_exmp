num_str = "0123456789"
num_x = num_str[2:6]
print(num_x)
num_x = num_str[2:]
print(num_x)
num_x = num_str[0:6]
print(num_x)
num_x = num_str[:]
print(num_x)
num_x = num_str[::2]
print(num_x)
num_x = num_str[1::2]
print(num_x)
num_x = num_str[-1]
print(num_x)
num_x = num_str[2:-1]
print(num_x)
num_x = num_str[-2:]
print(num_x)
#逆序切片/步长-1表示向左开始切，而开始-1表示从数字“9”开始切。两个组合使用达到了逆序输出的效果
num_x = num_str[-1::-1]
print(num_x)