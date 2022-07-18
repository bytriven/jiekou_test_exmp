import pprint

import pytest

from tool_pak.send_request import SendRquerst
from tool_pak.yaml_util import read_test_yaml, write_yaml, read_solo_yaml


class Test_Api:
    @pytest.mark.parametrize('caseinfo', read_test_yaml('/data/post_pwd_get_token.yaml'))
    def test_01_login(self, caseinfo):
        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'],
                                             json=caseinfo['request']['json'])
        result = res.json()
        if result['success'] == True:
            print('红红火火恍恍惚惚或或或或或或或或或或或或或')
            write_yaml({'token': result['data']}, '/data/save_token.yaml')
        else:
            print('错误原因：未输入正确账号密码')
            write_yaml({"token": result["data"]}, '/data/save_token.yaml')
            print('/n')

    @pytest.mark.parametrize("caseinfo", read_test_yaml('/data/No_token_get.yaml'))
    def test_02_Gettags(self, caseinfo):
        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'])
        result = res.json()
        sult = res.json()['data'][0]['tagName']
        pprint.pp(result)
        # self.titles = result.findall(r'【(.*?)】</h4>', self.page)这个就是正则表达式，带了？的表示以</h4>结尾，如果单纯的（.*）表示匹配任意字符
        # result=res.json()['data'][0]['id'],后面的[0]['id']是没有的，这里写是为了以后遇到这种情况如何处理做示范,注意JSON值里面有[]表单需要确定位置如[0][1][3]
        write_yaml(result, '/data/save_token.yaml')

    @pytest.mark.parametrize('caseinfo', read_test_yaml('/data/get_Out_off.yaml'))
    def test_api_03_get_OutOff(self, caseinfo):

        headers = {
            'Authorization': read_solo_yaml('token', '/data/save_token.yaml')
        }
        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'],
                                             headers=headers)
        result = res.json()
        pprint.pp('输出结果为：%s' % result)
