import os
import time

import pytest
from common.yaml_util import read_yaml, read_yaml2, write_yaml, clear_yaml, read_testcase_yaml

if __name__ == '__main__':
    #pytest.main(['-sv','test_api.py'])
    pytest.main(["-sv"])

    time.sleep(3)
    os.system('allure generate ./temps -o ./reports --clean')
    # -n=1.2.3.4.5...运行以多少个线程运行用例
    # -reruns=1.2.3.4...表示失败用例重跑次数
    # --html=./reports/reports.html

    # 三种运行方式，第一种就是上面的main方法，
    # 第二种是通过终端命令行的方式，具体的参数和main差不多，如：pytest -vs
    # 第三种是通过读取pytest.ini配置文件来执行测试用例
    # 不管使用main还是命令行都会自动去读取pytest.ini配置文件

    # #yaml_util练习调取
    # write_yaml({'age': '22', 'students': {'name': '张三', "numb": "123456"}})
    # print(read_yaml('students','name'))
    # print(read_yaml2())
    # clear_yaml()

    #测试用例数据驱动
    # print(read_testcase_yaml("/class_test_exrcise/get_token.yaml"))