import pytest
import requests

from common.send_request import SendRequest
from common.yaml_util import read_testcase_yaml
from common.yaml_util2 import write_yaml, read_yaml


class TestApi:

    @pytest.mark.run(order=2)
    def test_01_get_token(self):
        url = "http://106.55.103.86:8088/api/tags"
        # params = None,
        # res = requests.get(url=url)
        res = SendRequest().all_send_request(method='get', url=url)
        result = res.json()

        # 将json报文整个写入yaml中
        write_yaml(result)
        # print(res.json())

    # @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("caseinfo", read_testcase_yaml("/class_test_exrcise/get_token.yaml"))
    def test_02_post_login(self, caseinfo):
        # url = "http://106.55.103.86:8088/api/login"

        # 字典（对象）和json（字符串）的区别。
        # 如果参数的类型是字符串或者是只有键值对的字典。可以通过data传参。
        # #如:{ "id" :134, "name": "广东人"}
        # 如:把嵌套的字典转换成字符串(json. dumps ())
        # 如果参数的类型是只有键值对的字典或者是嵌套的字典，可以通过json传参。
        # #如:{ "id" :134, "name" : "广东人"}
        # 如:{ "tag" : { "id" :134, "name": "广东人"}}

        # json = {
        #     "account": "baiyang2",
        #     "password": "123456"
        # }

        # res = requests.post(url=url, json=json)

        # yaml数据驱动联系讲解
        print("_________")
        print(caseinfo["name"])
        print((caseinfo["request"]['method']))
        print(caseinfo['request']['url'])
        print(caseinfo['request']['headers'])
        print(caseinfo['request']['json'])
        print(caseinfo['validate'])

        name = caseinfo["name"]
        # method = caseinfo["request"]['method']
        # url = caseinfo['request']['url']
        headers = caseinfo['request']['headers']
        # params = caseinfo['request']['json']
        validate = caseinfo['validate']
        res = SendRequest().all_send_request(method=caseinfo['request']['method'], url=caseinfo['request']['url'], json=caseinfo['request']['json'])
        result = res.json()
        # print(res.json()["data"])
        if "success"==True:
            write_yaml({"token": result["data"]})
        else:
            print('错误原因：未输入正确账号密码')
            write_yaml({"token": result["data"]})
            print('/n')

    @pytest.mark.run(order=3)
    def test_03_get_OutOff(self):
        url = "http://106.55.103.86:8088/api/logout"
        headers = {
            "Authorization": read_yaml('token')
        }
        # response_json = requests.get(url=url, headers=headers)
        response_json = SendRequest().all_send_request(method='get', url=url, headers=headers)
        # print(response_json.json())
        # print(response_json.json()["success"])

# if __name__ == '__main__':
#     pytest.main(['-sv', 'test_api.py'])

# pytest.main(['-sv', '-m', 'smoke', 'test_api.py'])
