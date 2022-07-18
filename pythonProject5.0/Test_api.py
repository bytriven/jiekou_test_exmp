import pytest

from tool_pak.send_request import SendRquerst
from tool_pak.yaml_util import read_test_yaml, write_yaml, read_solo_yaml


class Test_api:
    @pytest.mark.parametrize("caseinfo",read_test_yaml('/data/post_pwd_get_token.yaml'))
    def test_01_login(self, caseinfo):
        res = SendRquerst().all_send_request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'],
                                             json=caseinfo['request']['json'])
        result =res.json()
        if result['success'] ==True:
            print('红红火火恍恍惚惚或或或或或或或或或或或或或')
            write_yaml({'token':result['data']},'/data/save_token.yaml')
        else:
            print('错误原因：未输入正确账号密码')
            write_yaml({"token": result["data"]}, '/data/save_token.yaml')
            print('/n')

    @pytest.mark.parametrize("caseinfo", read_test_yaml('/data/No_token_get.yaml'))
    def test_02_Gettags(self, caseinfo):
        res = SendRquerst.sess.request(method=caseinfo['request']['method'],url=caseinfo['request']['url'])
        result=res.json()
        write_yaml(result,'/data/save_token.yaml')

    @pytest.mark.parametrize('caseinfo',read_test_yaml('/data/get_Out_off.yaml'))
    def test_api_03_get_OutOff(self,caseinfo):
        headers={
            'Authorization':read_solo_yaml('token','/data/save_token.yaml')
        }
        res=SendRquerst.sess.request(method=caseinfo["request"]['method'], url=caseinfo['request']['url'], headers=headers)
        result=res.json()
        print('输出结果为 %s'%result)