from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
"""
pokemonType relationship ??
"""


class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float)
    catch_rate = db.Column(db.Float)
    captured = db.Column(db.Boolean)

    items = db.relationship(
        'Item', back_populates='pokemon', cascade="all, delete")

    def to_dict(self):
        moves = self.moves.split(',')

        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'moves': [move for move in moves]
        }


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    image_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey(
        'pokemons.id'), nullable=False)
    pokemon = db.relationship("Pokemon", back_populates='items')


class PokemonType(db.Model):
    __tablename__ = 'pokemon_types'
    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String(255), nullable=False)
