from flask import Blueprint, render_template, redirect
from ..models import db, Pokemon

pokemon_routes = Blueprint('pokemon', __name__, url_prefix="/api/pokemon")


@pokemon_routes.route("/")
def get_pokemon():
    pokemons = Pokemon.query.all()
    pokemon_response = [pokemon.to_dict() for pokemon in pokemons]
    return pokemon_response
