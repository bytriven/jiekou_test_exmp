a=[0,2,3]
print(id(a))
a.append("999")
a.append({
        "name":"白杨",
        "age":"18",
        " QQ":"123."
        })
#输出列表元素
print(a[3])
#索引列表内容index
print(a.index("999"))
#将字典从列表中剥离并输出key=value值
_dict=a[4]
print(_dict["name"])