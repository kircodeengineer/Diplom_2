from faker import Faker


class User:
    @staticmethod
    def create_user_data():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return reg_data

    @staticmethod
    def create_user_data_no_email():
        fake = Faker()

        reg_data = {
            "password": fake.password(),
            "name": fake.name()
        }
        return reg_data

    @staticmethod
    def create_user_data_no_password():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "name": fake.name()
        }
        return reg_data

    @staticmethod
    def create_user_data_no_name():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password()
        }
        return reg_data