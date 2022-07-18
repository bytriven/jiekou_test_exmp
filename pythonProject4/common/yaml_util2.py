import os

import yaml


# def read_yaml(n,k):
def read_yaml(key):
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8") as f:
        value = yaml.load(f,yaml.FullLoader)#直接写入参数就可以了，不用像视屏一样还要stream=f，loader=yaml...
        # try:
        #     #判断传入的n是否在存在
        #     if n in value.keys():
        #         return value[n][k]
        #     else:
        #         print(f"n：{n}不存在")
        # except Exception as e :
        #     print(f"key值{e}不存在")
        return value[key]

def read_yaml2():
    with open(os.getcwd() + "/extract.yaml", encoding="utf-8") as f:
        value = yaml.load(f,yaml.FullLoader)#直接写入参数就可以了，不用像视屏一样还要stream=f，loader=yaml...
        return value

#写入yaml文件
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",encoding='utf-8',mode='a') as f:
        yaml.dump(data,f,allow_unicode=True)

def clear_yaml():
    with open(os.getcwd()+'/extract.yaml',encoding='utf-8',mode='w')as f:
        f.truncate()
