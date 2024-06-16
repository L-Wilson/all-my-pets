from flask import Flask, request, jsonify
from datetime import datetime
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)


pets = []
id_counter = 1

@app.route('/static/openapi.yml')
def openapi():
    with open('openapi/openapi.yml', 'r') as f:
        return f.read()


@app.route('/pets', methods=['POST'])
def create_pet():
    global id_counter
    data = request.json
    if any(pet['name'] == data['name'] for pet in pets):
        return jsonify({'error': 'Pet already exists! Try another name'}), 409
    pet = {
        'id': id_counter,
        'name': data['name'],
        'createdAt': datetime.now()
    }
    pets.append(pet)
    id_counter += 1
    return jsonify(pet), 201


@app.route('/pets', methods=['GET'])
def get_all_pets():
    return jsonify(pets)


@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    f"Received request for pet_id: {pet_id}"
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
    if pet is not None:
        return jsonify(pet)
    return jsonify({'error': 'Pet not found'}), 404


@app.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    data = request.json
    if any(pet['name'] == data['name'] for pet in pets):
        return jsonify({'error': 'You already have a pet with that name! Each pet is special, they should each have their own name. Try again'}), 409
    pet = next((pet for pet in pets if pet['id'] == pet_id), None)
    if pet:
        pet['name'] = data.get('name', pet['name'])
        return jsonify(pet)
    return jsonify({'error': 'Pet not found'}), 404


@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    global pets
    pets = [pet for pet in pets if pet['id'] != pet_id]
    return '', 204



# OpenAPI/Swagger docs
SWAGGER_URL = '/api/docs'
API_URL = '/static/openapi.yml'  # Path to OpenAPI YAML file

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "My Pets API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


