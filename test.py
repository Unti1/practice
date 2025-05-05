import random
import uuid

from faker import Faker
from pydantic import ValidationError
from enums import RoleEnum
from schemas.user import UserPD
from settings.config import settings

faker = Faker()

if __name__ == '__main__':
    # print(str(uuid.uuid4()))
    # print(settings.ROOT_PATH)
    # print(settings.PG_DB)
    users_data = {
        'username': 'Qweasd',
        'password': 'Qweasdzxc1!',
        'email': faker.email(),
        'profile': {
            'phone': faker.basic_phone_number(),
            'role': random.choice(list(RoleEnum))
            },
    }
    try:    
        u = UserPD(**users_data)
        print(u)
        print(dict(u))
    except ValidationError as e:
        print(e.errors())
        error_msgs = [error['msg'] for error in e.errors()]
        print(error_msgs)
    
    
    