import json
from flask import jsonify, request


def get_all_users():
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return jsonify(data)


def get_user_by_id(id):
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for item in data["usuarios"]:
        if item["id"] == id:
            return jsonify(item)
    return jsonify({"message": "Não foi possível encontrar esse usuário!"})


def get_user_by_name(nome):
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    users = []
    for item in data["usuarios"]:
        if item["nome"].lower() == nome.lower():
            users.append(item)
    if users:
        return jsonify(users[0])
    else:
        return jsonify({"error": "User not found"}), 404


def add_user():
    new_data = request.get_json()
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    new_data["id"] = len(data["usuarios"]) + 1
    data["usuarios"].append(new_data)
    with open("data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    return jsonify({"message": "Cadastrado com sucesso!"}), 201


def update_user(id):
    updated_data = request.get_json()
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for item in data["usuarios"]:
        if item["id"] == id:
            item.update(updated_data)
            with open("data.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file)
            return jsonify({"message": "Usuário atualizado com sucesso!"})
    return jsonify({"message": "Usuário não encontrado!"}), 404


def delete_user(id):
    with open("data.json", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for item in data["usuarios"]:
        if item["id"] == id:
            data["usuarios"].remove(item)
            with open("data.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file)
            return jsonify({"message": "Usuário deletado com sucesso!"})
    return jsonify({"message": "Usuário não encontrado!"}), 404
