class Config:
    pass

class DevelopmentConfig(Config):
    #DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    # Database configuration
    #SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False

config = {
    'development' : DevelopmentConfig
}