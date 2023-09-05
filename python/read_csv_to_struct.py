import csv
from dataclasses import dataclass


@dataclass
class User:
    # TODO: make this correctly parse/convert the types.
    id: int
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    sallary: int
    favorite_animal: str


filepath = "../data/mock_data_from_mockaroo.csv"

with open(filepath, 'r') as f:
    reader = csv.DictReader(f)
    users: list[User] = []
    for row in reader:
        new_user = User(**row)
        users.append(new_user)
    print(users[1])
