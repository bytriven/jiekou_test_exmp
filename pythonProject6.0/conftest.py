import os
from os.path import dirname

import pytest

from tool_pak.yaml_util import clear_yaml


@pytest.fixture(scope='session',autouse=True)
def exe_assert():
    clear_yaml('/data/save_token.yaml')
    l=os.path.basename('save_token.yaml')
    # ls=os.path.dirname('tool_pak')这个是输出文件夹
    print('\n')
    print('yaml已清除，清除对象为：%s' %l)