from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    email: str
    account_id: int

    @field_validator('account_id')
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f'account_id must be postive: {value}')
        return value

user = User(name='Afiz', email='afiz@gmail.com', account_id=1234)
print(user)

user1 = User(name='Afiz', email='afiz@gmail.com', account_id=-10)
print(use1)