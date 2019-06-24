# pylint: disable=W0613
"""
	테스트코드 실행을 위한 테스트 코드
"""

import pytest

@pytest.mark.unit
def test_code(flask_app):
    """ 테스트 코드 """
    print("hi")
    assert True
