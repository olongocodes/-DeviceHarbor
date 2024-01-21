from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db, bcrypt
from flask_cors import CORS

from productorders import (
    OrderProductResource, 
    AdminProductOrdersResource, 
    ProductOrderResource, 
    UserOrdersResource)



from resources import (
    ProductResource,
    AdminProductResource,
    UserRegistrationResource,
    UserLoginResource,
    RefreshTokenResource,
    UserResource
)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deviceharbor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies'] 
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  
app.config['JWT_COOKIE_SECURE'] = False  
app.config['JWT_REFRESH_COOKIE_PATH'] = '/refresh'  
app.config['JWT_REFRESH_COOKIE_SECURE'] = False  
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = False  

api = Api(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)
db.init_app(app)
bcrypt.init_app(app)
CORS(app)

with app.app_context():
    db.create_all()

api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')
api.add_resource(RefreshTokenResource, '/refresh')
api.add_resource(ProductResource, '/products', '/products/<int:product_id>')
api.add_resource(AdminProductResource, '/products/<int:product_id>')
api.add_resource(UserResource, '/user')
api.add_resource(OrderProductResource, '/order')
api.add_resource(ProductOrderResource, '/productorders/<int:order_id>')
api.add_resource(AdminProductOrdersResource, '/productorders', '/productorders/<int:order_id>')
api.add_resource(UserOrdersResource, '/userorders', '/userorders/<int:order_id>')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)