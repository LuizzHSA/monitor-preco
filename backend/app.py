from flask import Flask
from flask_cors import CORS
from config import Config
from database.connection import init_db
from apscheduler.schedulers.background import BackgroundScheduler
from jobs.verificador import iniciar_verificacao_precos

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    CORS(app)
    
    init_db(app)
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=iniciar_verificacao_precos,
        trigger='interval',
        hours=1,
        id='verificacao_precos',
        name='Verificação automática de preços',
        replace_existing=True
    )
    scheduler.start()
    
    from routes import produto_bp, fornecedor_bp, preco_bp, alerta_bp
    app.register_blueprint(produto_bp, url_prefix='/api/produtos')
    app.register_blueprint(fornecedor_bp, url_prefix='/api/fornecedores')
    app.register_blueprint(preco_bp, url_prefix='/api/precos')
    app.register_blueprint(alerta_bp, url_prefix='/api/alertas')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)