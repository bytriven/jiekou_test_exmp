import os
import yaml


def read_testcase_yaml(yaml_path):
    with open(os.getcwd() + yaml_path, encoding='utf-8') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


def write_yaml(data, pro_yaml_path):
    with open(os.getcwd() + pro_yaml_path, encoding='utf-8', mode='a') as f:
        yaml.dump(data, f, allow_unicode=True)


def read_token_yaml(data, yaml_path):
    with open(os.getcwd() + yaml_path, encoding='utf-8') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value[data]


def clear_yaml(yaml_path):
    with open(os.getcwd()+yaml_path,encoding='utf-8',mode='w')as f:
        f.truncate()