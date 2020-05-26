"""
Module of flask config
Author: Po-Chun, Lu

"""
import os


class Config:
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    TIME_ZONE = os.environ.get("TIME_ZONE", 8)
    SPARK_SOURCE_FILE = os.environ.get("SPARK_SOURCE_FILE", "job.py")


class DevelopmentConfig(Config):
    """"configuration class for dev env"""

    DEBUG = True


class TestingConfig(Config):
    """"configuration class for testing env"""

    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """"configuration class for staging env"""

    DEBUG = True


class ProductionConfig(Config):
    """"configuration class for prod env"""

    DEBUG = False
    TESTING = False


APP_CONFIG = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
