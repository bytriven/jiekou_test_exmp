import requests


class SendRquerst:
    sess=requests.Session()
    def all_send_request(self,method,url,**kwargs):
        print("////////////////测试开始//////////////")
        print("接口地址：%s" % url)
        print("请求方式：%s" % method)
        res = SendRquerst.sess.request(method,url,**kwargs)
        if 'json' in kwargs.keys():
            print('请求json参数：%s' % kwargs['json'])
        elif 'params' in kwargs.keys():
            print('请求params参数：%s' % kwargs['params'])
        elif 'data' in kwargs.keys():
            print('请求data参数：%s' % kwargs['data'])
        elif 'file' in kwargs.keys():
            print('请求file参数：%s' % kwargs['file'])
        elif 'headers' in kwargs.keys():
            print('请求头headers参数：%s' % kwargs['headers'])
        print("返回接口值:%s" % res.json())
        print("-------------------测试结束----------------")
        print('\n')
        return res