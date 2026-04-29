from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
        try:
            with open('schema.sql', 'r') as f:
                schema = f.read()
                db.session.execute(schema)
                db.session.commit()
        except Exception as e:
            print(f"Erro ao criar schema: {e}")