from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Product, ProductOrder

class OrderProductResource(Resource):
    @jwt_required() 
    def post(self):
        try:
            current_user = User.query.filter_by(username=get_jwt_identity()).first()

            if not current_user:
                return {"message": "User not found."}, 404

            data = request.get_json()
            product_id = data.get('product_id')
            quantity = data.get('quantity')

            if not product_id or not quantity:
                return {"error": "Product ID and quantity are required."}, 400

            product = Product.query.get(product_id)
            if not product:
                return {"message": "Product not found."}, 404

            if quantity > product.quantity:
                return {"error": "Not enough quantity available for the product."}, 400

            # Update product quantity
            product.quantity -= quantity

            # Create a new product order
            new_order = ProductOrder(quantity=quantity, user=current_user, product=product)
            db.session.add(new_order)
            db.session.commit()

            return {"message": "Product ordered successfully."}, 201
        except Exception as e:
            return {"error": str(e)}, 500

class ProductOrderResource(Resource):
    @jwt_required()
    def get(self, order_id):
        try:
            current_user = User.query.filter_by(username=get_jwt_identity()).first()

            if not current_user:
                return {"message": "User not found."}, 404

            order = ProductOrder.query.get(order_id)
            if not order:
                return {"message": "Order not found."}, 404

            return {
                "order_id": order.id,
                "quantity": order.quantity,
                "user_id": order.user_id,
                "product_id": order.product_id
            }
        except Exception as e:
            return {"error": str(e)}, 500

class AdminProductOrdersResource(Resource):
    @jwt_required()
    def get(self, order_id=None):
        try:
            current_user = User.query.filter_by(username=get_jwt_identity()).first()

            if not current_user or current_user.role != 'admin':
                return {"message": "Access denied. Admins only."}, 403

            if order_id:
                order = ProductOrder.query.get(order_id)
                if not order:
                    return {"message": "Order not found."}, 404

                return {
                    "order_id": order.id,
                    "quantity": order.quantity,
                    "user_id": order.user_id,
                    "product_id": order.product_id
                }
            else:
                orders = ProductOrder.query.all()
                return [
                    {
                        "order_id": order.id,
                        "quantity": order.quantity,
                        "user_id": order.user_id,
                        "product_id": order.product_id
                    }
                    for order in orders
                ]
        except Exception as e:
            return {"error": str(e)}, 500

    @jwt_required()
    def put(self, order_id):
        try:
            current_user = User.query.filter_by(username=get_jwt_identity()).first()

            if not current_user:
                return {"message": "User not found."}, 404

            order = ProductOrder.query.get(order_id)
            if not order:
                return {"message": "Order not found."}, 404

            data = request.get_json()
            new_quantity = data['quantity']

            # Restore previous quantity to the product
            order.product.quantity += order.quantity

            # Deduct the updated quantity from the product
            if new_quantity > order.product.quantity:
                return {"error": "Not enough quantity available for the product."}, 400

            order.product.quantity -= new_quantity
            order.quantity = new_quantity

            db.session.commit()

            return {"message": "Product order updated successfully."}
        except Exception as e:
            return {"error": str(e)}, 500

    @jwt_required()
    def delete(self, order_id):
        try:
            current_user = User.query.filter_by(username=get_jwt_identity()).first()

            if not current_user or current_user.role != 'admin':
                return {"message": "Access denied. Admins only."}, 403

            order = ProductOrder.query.get(order_id)
            if not order:
                return {"message": "Order not found."}, 404

            # Restore quantity to the product
            order.product.quantity += order.quantity

            db.session.delete(order)
            db.session.commit()

            return {"message": "Product order deleted successfully."}
        except Exception as e:
            return {"error": str(e)}, 500
class UserOrdersResource(Resource):
    @jwt_required()
    def get(self, order_id=None):
        try:
            current_user = User.query.filter_by(username=get_jwt_identity()).first()

            if not current_user:
                return {"message": "User not found."}, 404

            if order_id:
                order = ProductOrder.query.filter_by(user_id=current_user.id, id=order_id).first()

                if not order:
                    return {"message": "Order not found."}, 404

                return {
                    "order_id": order.id,
                    "quantity": order.quantity,
                    "user_id": order.user_id,
                    "product_id": order.product_id
                }
            else:
                orders = ProductOrder.query.filter_by(user_id=current_user.id).all()
                return [
                    {
                        "order_id": order.id,
                        "quantity": order.quantity,
                        "user_id": order.user_id,
                        "product_id": order.product_id
                    }
                    for order in orders
                ]
        except Exception as e:
            return {"error": str(e)}, 500