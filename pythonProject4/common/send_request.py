import requests


class SendRequest:
    sess = requests.session()

    def all_send_request(self, method, url, **kwargs):
        print()
        print('---------接口测试开始----------')
        print('接口地址：%s' % url)
        print('请求方式：%s' % method)
        # if '' in kwargs.keys():
        #     print('请求参数：无')
        # else:
        #     print('请求参数：%s' % kwargs)
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
        res = SendRequest.sess.request(method, url, **kwargs)
        print('接口返回值：%s' % res.json())
        print('---------接口测试结束----------')
        print('\n')
        return res
