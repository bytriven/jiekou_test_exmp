xiaoming = {"name":"小明",
            "age":18}
#1.统计键值对的数量
print(len(xiaoming))
#2.合并字典/注意：如果被合并的字典包含已存在的减值对，那么会覆盖原有的键值对
temp = {"weight":120,
        "age":20}
xiaoming.update(temp)
print(xiaoming)
#3.清空字典
xiaoming.clear()
print(xiaoming)