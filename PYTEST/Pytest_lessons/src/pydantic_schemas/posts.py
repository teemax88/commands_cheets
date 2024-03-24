from pydantic import BaseModel, validator


class Post(BaseModel):
    id: int
    title: str

    """
    способ проверки без написания валидатора
    id: int = Field(le=2)    

    если в ответе есть параметр типа _name, то применяем алиас
    name: str = Field(alias="_name")
    """

    @validator("id")
    def check_that_id_is_less_than_two(cls, v):
        if v > 3:
            raise ValueError("Id is not less than two")
        else:
            return v
