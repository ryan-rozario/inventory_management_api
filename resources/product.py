from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from database.models import Product, User
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, ProductAlreadyExistsError, InternalServerError, \
UpdatingProductError, DeletingProductError, ProductNotExistsError


class ProductsApi(Resource):
    def get(self):
        products = Product.objects().to_json()
        return Response(products, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            product =  Product(**body, added_by=user)
            product.save()
            user.update(push__products=product)
            user.save()
            id = product.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProductAlreadyExistsError
        except Exception as e:
            raise InternalServerError
        
class ProductApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            product = Product.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            Product.objects.get(id=id).update(**body)
            return '', 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise ProductAlreadyExistsError
        except Exception as e:
            raise InternalServerError
    
    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            product = Product.objects.get(id=id, added_by=user_id)
            product.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingProductError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            products = Product.objects.get(id=id).to_json()
            return Response(products, mimetype="application/json", status=200)
        except DoesNotExist:
            raise DeletingProductError
        except Exception:
            raise InternalServerError