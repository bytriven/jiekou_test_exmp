import pytest

from tool_pak.yaml_util import clear_yaml


@pytest.fixture(scope='session',autouse=True)
def exe_assert():
    clear_yaml('/data/save_token.yaml')
    #这个语法还要看软件路径层级关系，一般都是放在根目录上，才能起到全局clear的作用