from flask import Blueprint, jsonify, request
import json
import os

transaction_blueprint = Blueprint('transactions', __name__)

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
    transaction = transactions_data.get(id, None)
    return jsonify(transaction), 200

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    new_transaction = request.json 
    transactions_data[new_transaction['id']] = new_transaction
    return jsonify(new_transaction), 201  

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    updated_transaction = request.json 
    transactions_data[id] = updated_transaction
    return jsonify(updated_transaction), 200


@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    deleted_transaction = request.json
    transactions_data[id] = deleted_transaction
    return jsonify(deleted_transaction),200


@transaction_blueprint.route('/transactions', methods=['GET'])
def get_all_transactions():
    return jsonify(transactions_data), 200
