'''print("hello world")
sum=1
a=1
while a<10:
    if a%2
    sum=sum+a
    a=a+1
    print('加数',sum)

print(sum) '''
#2022.2.19(简单的函数嵌套和计算)
jiage=float(input("请输入价格："))
jinshu=float(input("请输入斤数："))
geiqian=jiage * jinshu
print("你需要给钱：",geiqian,"元")
#格式化输出范例

print("输入的价格是: %.2f元/斤,输入的斤数是： %.2f斤,总价是： %.2f元" %(jiage,jinshu,geiqian))

name = "小明"
print("我的名字叫 %s，请多多关照！" % name)

students_num=1222222
print("我的学号是 %09d" % students_num)

scale = 0.22134
print("输出的数据比例是 %.4f%%" % (scale * 100))#如何输出百分号，以及在print里面进行练乘