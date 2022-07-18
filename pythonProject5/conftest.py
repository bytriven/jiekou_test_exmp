import pytest

from tool_pak.yaml_util import clear_yaml


@pytest.fixture(scope='session',autouse=True)
def exe_assert():
    clear_yaml('/save_tagsData.yaml')
    clear_yaml('/data/save_token.yaml')