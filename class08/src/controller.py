import requests
from src.schema import PokemonSchema
from src.db import SessionLocal, engine, Base
from src.models import Pokemon


Base.metadata.create_all(bind=engine)


def get_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    print(response)
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchema(
            name=data['name'], 
            type=types, 
            weight=data['weight'],)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, 
                             type=pokemon_schema.type,
                             weight=pokemon_schema.weight)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon