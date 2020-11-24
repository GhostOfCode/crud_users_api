from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    username: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'username': 'Iron Man',
                'first_name': 'Tony',
                'last_name': 'Stark',
                'password': 'BestIronMan4Ever'
                }
        }


class UpdateUserModel(BaseModel):
    username: str = Field()
    first_name: str = Field()
    last_name: str = Field()
    password: str = Field()

    class Config:
        schema_extra = {
            "example": {
                'username': 'War Machine',
                'first_name': 'James',
                'last_name': 'Rhodes',
                'password': 'BestFriend4Ever'
                }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
