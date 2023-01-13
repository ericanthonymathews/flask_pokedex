from app.models import db, Pokemon, Item, PokemonType
from app import app
from random import choice, randint
from dotenv import load_dotenv
load_dotenv()

with app.app_context():

    db.drop_all()
    db.create_all()

    pokemon1 = Pokemon(
        number=1,
        image_url='/images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type='grass',
        moves="tackle,vine whip",
        captured=True
    )

    pokemon2 = Pokemon(
        number=2,
        image_url='/images/pokemon_snaps/2.svg',
        name='Ivysaur',
        attack=62,
        defense=63,
        type='grass',
        moves='tackle,vine whip,razor leaf',
        captured=True
    )

    pokemon3 = Pokemon(
        number=3,
        image_url='/images/pokemon_snaps/3.svg',
        name='Venusaur',
        attack=82,
        defense=83,
        type='grass',
        moves='tackle,vine whip,razor leaf',
        captured=True
    )

    pokemon4 = Pokemon(
        number=4,
        image_url='/images/pokemon_snaps/4.svg',
        name='Charmander',
        attack=52,
        defense=43,
        type='fire',
        moves='scratch,ember,metal claw',
        captured=True
    )

    pokemon5 = Pokemon(
        number=5,
        image_url='/images/pokemon_snaps/5.svg',
        name='Charmeleon',
        attack=64,
        defense=58,
        type='fire',
        moves='scratch,ember,metal,claw,flamethrower',
        captured=True
    )

    pokemon6 = Pokemon(
        number=6,
        image_url='/images/pokemon_snaps/6.svg',
        name='Charizard',
        attack=84,
        defense=78,
        type='fire',
        moves='flamethrower,wing attack,slash,metal claw',
        captured=True
    )

    pokemon7 = Pokemon(
        number=7,
        image_url='/images/pokemon_snaps/7.svg',
        name='Squirtle',
        attack=48,
        defense=65,
        type='water',
        moves='tackle,bubble,water gun',
        captured=True
    )

    pokemon8 = Pokemon(
        number=8,
        image_url='/images/pokemon_snaps/8.svg',
        name='Wartortle',
        attack=63,
        defense=80,
        type='water',
        moves='tackle,bubble,water gun,bite'
    )

    pokemon9 = Pokemon(
        number=9,
        image_url='/images/pokemon_snaps/9.svg',
        name='Blastoise',
        attack=83,
        defense=100,
        type='water',
        moves='hydro pump,bubble,water gun,bite'

    )

    pokemon10 = Pokemon(
        number=10,
        image_url='/images/pokemon_snaps/10.svg',
        name='Caterpie',
        attack=30,
        defense=35,
        type='bug',
        moves='tackle'


    )

    pokemon12 = Pokemon(
        number=12,
        image_url='/images/pokemon_snaps/12.svg',
        name='Butterfree',
        attack=45,
        defense=50,
        type='bug',
        moves='confusion,gust,psybeam,silver wind'

    )

    pokemon13 = Pokemon(
        number=13,
        image_url='/images/pokemon_snaps/13.svg',
        name='Weedle',
        attack=35,
        defense=30,
        type='bug',
        moves='poison sting'


    )

    pokemon16 = Pokemon(
        number=16,
        image_url='/images/pokemon_snaps/16.svg',
        name='Pidgey',
        attack=45,
        defense=40,
        type='normal',
        moves='tackle,gust'


    )

    pokemon17 = Pokemon(
        number=17,
        image_url='/images/pokemon_snaps/17.svg',
        name='Pidgeotto',
        attack=60,
        defense=55,
        type='normal',
        moves='tackle,gust,wing attack'
    )

    pokemon18 = Pokemon(
        number=18,
        image_url='/images/pokemon_snaps/18.svg',
        name='Pidgeot',
        attack=80,
        defense=75,
        type='normal',
        moves='tackle,gust,wing attack'
    )

    all_pokemons = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7,
                    pokemon8, pokemon9, pokemon10, pokemon12, pokemon13, pokemon16, pokemon17, pokemon18]

    add_pokemons = [db.session.add(pokemon) for pokemon in all_pokemons]
    db.session.commit()
    print("Pokemons Seeded")

    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]

    item1 = Item(
        pokemon_id=pokemon1.id,
        name="Super Potion",
        price=randint(100),
        happiness=randint(100),
        image_url=choice(images)
    )
    item2 = Item(
        pokemon_id=pokemon2.id,
        name="Potion",
        price=randint(100),
        happiness=randint(100),
        image_url=choice(images)
    )
    item3 = Item(
        pokemon_id=pokemon4.id,
        name="Pokemon Egg",
        price=randint(100),
        happiness=randint(100),
        image_url=choice(images)
    )
    item4 = Item(
        pokemon_id=pokemon1.id,
        name="Pokemon Berry",
        price=randint(100),
        happiness=randint(100),
        image_url=choice(images)
    )
