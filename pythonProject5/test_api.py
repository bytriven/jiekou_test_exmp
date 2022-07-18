import pytest
import json

from tool_pak.send_request import SendRquerst
from tool_pak.yaml_util import read_testcase_yaml, write_yaml, read_token_yaml, clear_yaml


class TestApi:

    @pytest.mark.parametrize('caseinfo', read_testcase_yaml('/data/post_pwd_get_token.yaml'))
    def test_api_01_login(self, caseinfo):

        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'],
                                             json=caseinfo['request']['json'])
        result = res.json()
        print('输出token为：%s' % result.values())
        print('输出code为：%s' % result['code'])
        print('输出result为：%s' % result)
        if result['success'] == True:
            print('红红火火恍恍惚惚或或或或或或或或或或或或或')
            write_yaml({"token": result['data']}, '/data/save_token.yaml')
        else:
            print('错误原因：未输入正确账号密码')
            write_yaml({"token": result["data"]}, '/data/save_token.yaml')
            print('/n')

    @pytest.mark.parametrize('caseinfo', read_testcase_yaml('/data/No_token_get.yaml'))
    def test_api_02_Gettags(self,caseinfo):
        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'])
        result = res.json()
        write_yaml(result, '/save_tagsData.yaml')

    @pytest.mark.parametrize('caseinfo', read_testcase_yaml('/data/get_Out_off.yaml'))
    def test_api_03_get_OutOff(self,caseinfo):
        #token=json.dumps(read_testcase_yaml('/data/save_token.yaml'))
        print('\n')
        #print("你的值： %s" % token)
        headers = {
            "Authorization": read_token_yaml('token','/data/save_token.yaml')
        }
        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'], headers=headers)#headers=caseinfo['request']['headers']  #headers=headers['Authorization']
        result=res.json()
        print('退出账户结果为结果为：%s' % result)
    # def test_03_get_OutOff(self):
    #     print("请求token： %s" %read_testcase_yaml('/data/save_token.yaml'))
    #     url = "http://106.55.103.86:8088/api/logout"
    #     # headers = {
    #     #     "Authorization": read_testcase_yaml('/data/save_token.yaml')
    #     # }
    #     # response_json = requests.get(url=url, headers=headers)
    #     # response_json = SendRquerst().all_send_request(method='get', url=url, headers=headers)
    #     res = SendRquerst().all_send_request(method='get', url=url)
    #     result = res.json()
    #     print(result)