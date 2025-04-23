import random
import uuid

from faker import Faker
from enums import RoleEnum
from settings.config import settings

faker = Faker()

if __name__ == '__main__':
    # print(str(uuid.uuid4()))
    # print(settings.ROOT_PATH)
    # print(settings.PG_DB)
    users_data = {
        'username': faker.user_name(),
        'password': faker.password(),
        'email': faker.email(),
        'phone': faker.basic_phone_number(),
        'role': random.choice(list(RoleEnum)),
    }