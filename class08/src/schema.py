from pydantic import BaseModel


class PokemonSchema(BaseModel):
    name: str
    type: str
    weight: int

    class Config:
        orm_mode = True