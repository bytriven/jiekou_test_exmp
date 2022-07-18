poem = ["登黄鹤楼",
        "王焕之",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
#居中对齐用center后面跟的是填充宽度和填充内容
for poem_str in poem :
    print("|%s|" % poem_str.center(10,"　"))
#向左对齐用ljust
for poem_str in poem :
    print("|%s|" % poem_str.ljust(10,"　"))
#向右对齐用rjust
for poem_str in poem :
    print("|%s|" % poem_str.rjust(10,"　"))