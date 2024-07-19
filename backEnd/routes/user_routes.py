from flask import Blueprint
from controllers.user_controller import (
    get_all_users,
    get_user_by_id,
    get_user_by_name,
    add_user,
    update_user,
    delete_user,
)

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/usuarios", methods=["GET"])
def get_users():
    return get_all_users()


@user_routes.route("/usuarios/<int:id>", methods=["GET"])
def get_user(id):
    return get_user_by_id(id)


@user_routes.route("/usuarios/nome=<nome>", methods=["GET"])
def get_user_by_name_route(nome):
    return get_user_by_name(nome)


@user_routes.route("/usuarios", methods=["POST"])
def add_user_route():
    return add_user()


@user_routes.route("/usuarios/<int:id>", methods=["PUT"])
def update_user_route(id):
    return update_user(id)


@user_routes.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_user_route(id):
    return delete_user(id)
