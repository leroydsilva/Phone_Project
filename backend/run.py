from config import DevConfig,ProdConfig
from app import create_app

if __name__ == '__main__':
    app=create_app(ProdConfig)
    app.run()