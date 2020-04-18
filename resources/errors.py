class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ProductAlreadyExistsError(Exception):
    pass

class UpdatingProductError(Exception):
    pass

class DeletingProductError(Exception):
    pass

class ProductNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "ProductAlreadyExistsError": {
         "message": "Product with given name already exists",
         "status": 400
     },
     "UpdatingProductError": {
         "message": "Updating product added by other is forbidden",
         "status": 403
     },
     "DeletingProductError": {
         "message": "Deleting product added by other is forbidden",
         "status": 403
     },
     "ProductNotExistsError": {
         "message": "Product with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     },
     "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
     }
}