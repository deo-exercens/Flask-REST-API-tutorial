# pylint: disable=C0103
"""
    configuration test
"""

class TestConfig:
    """ app/config 테스트 """
    @staticmethod
    def test_TestConfig(test_app, config_keys):
        """ TestConfig 테스트 """
        for key in config_keys:
            print(key)
            assert key in test_app.config

    @staticmethod
    def test_ContinuousIntegrationConfig(ci_app, config_keys):
        """ ContinuousIntegrationConfig 테스트 """
        for key in config_keys:
            print(key)
            assert key in ci_app.config

    @staticmethod
    def test_DevelopmentConfig(development_app, config_keys):
        """ DevelopmentConfig 테스트 """
        for key in config_keys:
            print(key)
            assert key in development_app.config
