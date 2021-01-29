from sqlalchemy import Column, VARCHAR
from models.base_model import BaseModel
from sqlalchemy.orm import validates


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', VARCHAR(length=200), nullable=False)
    description = Column('description', VARCHAR(length=400), nullable=False)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        elif not name.strip():
            raise ValueError("Name can't be empty!")
        elif len(name) > 200:
            raise ValueError("Name must contains less than 200 characters!")
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description must be string")
        if not description.strip():
            raise ValueError("Description can't be empty!")
        elif len(description) > 400:
            raise ValueError("Description must contains less than 400 characters!")
        return description

