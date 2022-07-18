xiaoming = {"name":"小明",
            "age":18,
            "gender":True,
            "weight":140,
            "high":1.75}
#1.取值
print(xiaoming["age"])
#2.增加/修改
xiaoming["age"]=20
print(xiaoming)
print("*" * 50)
#增加操作
xiaoming["score"] = 89
print(xiaoming)
print("*" * 50)
#3.删除
xiaoming.pop("name")
print(xiaoming)