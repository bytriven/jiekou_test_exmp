# import pytest
# from common.yaml_util import clear_yaml
#
# @pytest.fixture(scope='session',autouse=True)
# def exe_assert():
#     clear_yaml()
import pytest

from common.yaml_util import clear_yaml

@pytest.fixture(scope='session',autouse=True)
def exe_assert():

    clear_yaml()