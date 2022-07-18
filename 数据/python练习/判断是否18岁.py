#age=int(input("请输入年龄："))
'''if age>=18:
    print("你可以进入网吧，欢迎光临！")
else :
    print("你还未成年，不嗯呢该进入！")'''
#逻辑运算
'''if age>=18 and age<=100:
    print("你可以进入网吧，欢饮使用！")
else :
    print("你的年龄不正确，不允许进入！")'''
#判断考试成绩
python_score=float(input("输入你的python成绩："))
c_score=float(input("输入你的c语言成绩："))
avg = (python_score + c_score)/2
times = 3
if python_score > 60 and c_score > 60:
    print("考试通过。")
else :
    print("考试暂定未通过，正在计算平均分查看是否具有补考资格。")
    if avg > 60 :
        print("你还有 %d 次补考机会" % times)
        print("*" * 50)
    elif avg >= 55 and avg <= 60:
        times = times - 1
        print("你还有 %d 次补考机会" % times)
        print("*" * 50)
    elif avg >= 50 and avg < 55:
        times = times - 2
        print("你还有 %d次补考机会" % times)
        print("*" * 50)
    else :
        print("考试不通过,你的平均分是 %.2f 没有补考资格。" % avg)
        print("*" * 50)