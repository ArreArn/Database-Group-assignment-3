from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    publisher_id: int
    isbn: str
    year_published: int


@dataclass
class Publisher:
    id: int
    name: str
    address: str
    phone: str
    email: str


@dataclass
class Member:
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    date_of_membership: str

