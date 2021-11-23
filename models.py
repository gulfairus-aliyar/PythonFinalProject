from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=True)


class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coin_name = db.Column(db.String, unique=True, nullable=False)
    paragraphs = db.relationship("Paragraph", backref='coin', lazy=True)


class Paragraph(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coin_id = db.Column(db.Integer, db.ForeignKey("coin.id"), nullable=False)
    text = db.Column(db.String)
    summary = db.Column(db.String, nullable=True)
