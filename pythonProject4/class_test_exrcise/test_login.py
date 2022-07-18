import pytest


# 读取数据
def read_yaml():
    return ['百里', '贝帆', '星耀']


# 读取数据时就是这种写法了  @pytest.fixture(scope='function',aotuse=False,params=read_yaml())
# def exe_assert(request):
#     print('在用力之前执行：查询数据库用于断言')
#     yield request.param
#     print('在用例之后执行：查询数据库')

#     在需要执行的function内这样操作
# def test_register(self, exe_assert):
#     print('注册接口'+exe_assert)
@pytest.fixture(scope='function')  # 还有使用class类的内容，比如@pytest.fixture(scope='class')表示在类上调用，
# 此时若在后面添加autouse=True自动添加时直接就是全局调用，则不用使用@pytest.mark.usefixture('exe_assert')做手动调用
# 需要在单独的class或者function上使用，则要对应class或者function前，使用到@pytest.mark.usefixture('exe_assert')
# @pytest.fixture(scope='function',autouse=True)
def exe_assert():
    print('在用力之前执行：查询数据库用于断言')
    yield
    # yield '百里老师'
    print('在用例之后执行：查询数据库')


class Test_login:
    def test_login(self):
        print("登录接口")

    # def test_register(self, exe_assert):
    def test_register(self):
        print('注册接口')
        # print('注册接口'+exe_assert)

    def test_test(self):
        print('测试接口')


if __name__ == '__main__':
    pytest.main(['test.login.py'])

    # 快捷键换行，shift+回车
    # 多行注释  ctrl+/


