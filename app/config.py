import os
class Config:
    SECRET_KEY=os.urandom(32)

    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    DEBUG= True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfig(Config):
    DEBUG= False
    # postgresql:://username:password@localhost:portnumber/dbname
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:david@localhost:5432/flasktask"
    


projectConfig= {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}