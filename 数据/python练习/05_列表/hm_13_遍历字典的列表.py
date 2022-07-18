students = [
    {"name":"alex"},
    {"name":"lee"}
]
find_name = str(input("输入要查找的人："))
for stu_dict in students:
    
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break#这个很重要，可以跳出当前循环，不用继续执行下面的代码
else:
    print("抱歉没有找到 %s" % find_name)
print("循环结束")