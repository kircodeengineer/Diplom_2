class StatusCodes:
    CODE_200 = 200
    CODE_401 = 401
    CODE_403 = 403

class Messages:
    class CreateUser:
        USER_EXISTS = 'User already exists'
        EMPTY_FIELD = 'Email, password and name are required fields'

    class Login:
        INCORRECT_USER_DATA = 'email or password are incorrect'
