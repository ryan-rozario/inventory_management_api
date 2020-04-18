from .product import ProductsApi, ProductApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword

def initialize_routes(api):
    api.add_resource(ProductsApi, '/api/products')
    api.add_resource(ProductApi, '/api/products/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot')
    api.add_resource(ResetPassword, '/api/auth/reset')
