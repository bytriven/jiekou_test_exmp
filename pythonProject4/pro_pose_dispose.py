import pytest
#读取数据
def read_1():
    return ["百里",'北凡','星耀']
@pytest.fixture(scope='function',autouse=False,params=read_1())
def exe_assert(request):
    print('在用例之前执行：查询数据库用于断言')

    yield request.param#'百里老师'#加上这个可以用于后置处理,后面可以跟实际参数像这里的‘百里老师’，在具体函数内直接调用，如下.
                        # 当使用request返回read_yaml的值时候需要在上面声明一个request

    print('\n')
    print('在用例之后执行：查询数据库')

    #如果是session级别，那么不管开多少个py文件，都只会执行一次。比如我把pro_pose_dispose.py,test_api.py一起运行了，一共会有多条用例
    #但始终只会在用例报告的开头和结尾出现一次  print('在用例之前执行：查询数据库用于断言')和   print('在用例之后执行：查询数据库')。
    #这个作用就是用于接口自动化关联的封装


#@pytest.mark.usefixtures("exe_assert")这是用手动方式实现对fixture调用，由于是对类class应用，所以放在class上面，且上面的scope也要换成‘class’
class TestLogin:

    # def setup_class(self):
    #     print('每个类之前执行')
    #
    # def teardown_class(self):
    #     print('每个类之后执行')

    # def setup(self):
    #     print('每个用例之前执行')
    #
    # def teardown(self):
    #     print("每个用例之后执行")

    def test_01_login(self):
        print('这是登录接口')

    def test_02_register(self, exe_assert):
        print('这是注册接口：'+ exe_assert)

    def test_03_query(self):
        print('这是查询接口')
