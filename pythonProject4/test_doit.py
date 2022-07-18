import pytest

age = 16


class Test_doit:

    @pytest.mark.skip(reason="跳过01用例")
    def test_01(self):
        print("day02------test_day01")
        print('第1个执行')

    @pytest.mark.skipif(age >= 18, reason="age大于18跳过")
    def test_02(self):
        print("day02------test_day02")
        print('第2个执行')

    @pytest.mark.run(order=2)
    def test_03(self):
        print("day02------test_day03")
        print('第3个执行')

    # @pytest.mark.smoke
    # def test_smoke(self):
    #     print("冒烟测试。。。")
    #     print('第4个执行')

    @pytest.mark.run(order=1)
    def test_login(self):
        print("用户登录。。")
        print('第5个执行')

#
# if __name__ == '__main__':
#     pytest.main(['-sv', '-m', 'smoke', 'test_doit.py'])
