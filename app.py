from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///motivational_messages.db'
db = SQLAlchemy(app)

class MotivationalMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)

db.create_all()

# Rota para obter uma mensagem motivacional aleatória
@app.route('/mensagem_motivacional', methods=['GET'])
def obter_mensagem_motivacional():
    mensagem = random.choice(MotivationalMessage.query.all())
    return render_template(
        'mensagem_motivacional.html',
        mensagem=mensagem.message
    )

if __name__ == '__main__':
    app.run(debug=True)
