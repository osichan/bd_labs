from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .menu.dish_route import dish_bp
    from .menu.menu_dish_route import menu_dish_bp
    from .menu.menu_route import menu_bp
    from .object.comments_route import comments_bp
    from .object.entertainment_route import entertainment_bp
    from .object.hotel_route import hotel_bp
    from .object.object_route import object_bp
    from .object.restaurant_route import restaurant_bp
    from .person.buyer_route import buyer_bp
    from .person.person_route import person_bp
    from .person.seller_route import seller_bp

    app.register_blueprint(dish_bp)
    app.register_blueprint(menu_dish_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(entertainment_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(object_bp)
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(buyer_bp)
    app.register_blueprint(person_bp)
    app.register_blueprint(seller_bp)
