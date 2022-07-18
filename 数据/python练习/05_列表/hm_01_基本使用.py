name_list = ["zhangsan","lisi","wangwu"]

#取值和取索引
#1.list index out of range 列表索引超出范围
print(name_list[2])
#知道数据内容，想确定数据在列表中的位置
#使用index（索引）方法需要注意，如果传递数据不在列表中，程序会报错
print(name_list.index("wangwu"))
#2.修改.列表指定的索引超出范围，程序报错
#name_list[1] = "李四"
#print("程序输出名字是 %s," % name_list[1])
#3.增加   
#insert可以在列表的指定位置插入追加数据
name_list.insert(1,"王小二")
#append直接在列表末尾插入追加数据
name_list.append("美女")
print(name_list)
#extend可以把其他列表的完整内容插入到其他列表末尾
temp_list = ["孙悟空","猪八戒","沙悟净"]
name_list.extend(temp_list)
print(name_list)
#4。删除
print("*" * 50)
#remove可以从列表中删除指定的数据
name_list.remove("wangwu")
#pop如果不带索引参数，则默认弹出列表最后一项，类似弹栈的效果。如果带了索引参数，那么弹出对应数据
name_list.pop()
name_list.pop(1)
print(name_list)
#clear整个列表清空
print(name_list.clear())
#del 删除。关键字本质上是用来将一个变量从内存中删除,简单理解，就是可以直接使用删除列表名，即后续的代码就不能再使用这个变量
del temp_list[1]
print(temp_list)
