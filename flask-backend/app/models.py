from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Pokemon(db.Model): 
  __tablename__ = "pokemons"
  id = db.Column(db.Integer, primary_key=True)
  number = db.Column(db.Integer, unique=True, nullable=False)
  attack = db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  imageUrl = db.Column(db.String, nullable=False)
  name = db.Column(db.String(255), unique=True, nullable=False)
  type = db.Column(db.String(255), nullable=False)
  moves = db.Column(db.String(255), nullable=False)
  encounterRate = db.Column(db.Float)
  captured = db.Column(db.Boolean)







