from faker import Faker

faker = Faker()

def random_user():
    return {
        "username": faker.user_name(),
        "email": faker.email(),
        "uuid": faker.uuid4()
    }
