class StatusCodes:
    CODE_200 = 200
    CODE_400 = 400
    CODE_401 = 401
    CODE_403 = 403
    CODE_500 = 500

class Messages:
    INTERNAL_SERVER_ERROR = 'Internal Server Error'

    class CreateUser:
        USER_EXISTS = 'User already exists'
        EMPTY_FIELD = 'Email, password and name are required fields'

    class Login:
        INCORRECT_USER_DATA = 'email or password are incorrect'

    class ChangeUserData:
        NOT_AUTHORIZED = 'You should be authorised'

    class GetUserOrders:
        NOT_AUTHORIZED = 'You should be authorised'

    class CreateOrder:
        NO_INGREDIENTS_PROVIDED = "Ingredient ids must be provided"

class IngredientsData:
    VALID_HASH = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6e"]
    }

    NOT_VALID_HASH = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6f1", "61c0c5a71d1f82001bdaaa6e1"]
    }