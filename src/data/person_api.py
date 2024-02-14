from flask import Flask, request
from person_service import db_get_persons, db_get_person_by_id, db_create_person, db_update_person, db_delete_person
from attributes_service import db_get_attributes, db_get_attribute_by_id, db_create_attribute, db_update_attribute, db_delete_attribute
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

# Person database
@app.route('/person', methods=['GET'])
def get_all_person():
    try:  
        return db_get_persons()
    except:
        return {"error": "no data"}

@app.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    try:
        return db_get_person_by_id(id)
    except:
        return {"error": "no person with id %s" % id}

@app.route("/person", methods=['POST'])
def create_person():
    try: 
        data = request.get_json()
        name = data['name']
        age = data['age']
        student = data['student']
        db_create_person(name, age, student)
        return {"success": "created person: %s" % name}
    except:
        return {"error": "error creating person"}

@app.route("/person/<int:id>", methods=['PUT'])
def update_person(id):
    try:
        data = request.get_json()
        name = data['name']
        age = data['age']
        student = data['student']
        db_update_person(id, name, age, student)
        return {"success": "updated person"}
    except:
        return {"error": "error updating person"}

@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        return db_delete_person(id)
    except:
        return {"error": "no such person"}

# Attributes database
@app.route('/attributes', methods=['GET'])
def get_attributes():
    try:  
        return db_get_attributes()
    except:
        return {"error": "no data"}

@app.route('/attributes/<int:id>', methods=['GET'])
def get_attribute_by_id(id):
    try:
        return db_get_attribute_by_id(id)
    except:
        return {"error": "no attribute with id %s" % id}

@app.route("/attributes", methods=['POST'])
def create_attribute():
    try: 
        data = request.get_json()
        attribute_name = data['attribute_name']
        description = data['attribute_description']
        value = data['attribute_value']
        person_id = data['person_id']
        db_create_attributes(attribute_name, description, value, person_id)
        return {"success": "created attribute: %s" % attribute_name}
    except:
        return {"error": "error creating attribute"}
    

@app.route('/attributes/<int:id>', methods=['PUT'])
def update_attribute(id):
    try:
        data = request.get_json()
        attribute_name = data['attribute_name']
        description = data['attribute_description']
        value = data['attribute_value']
        person_id = data['person_id']
        db_update_attribute(id, attribute_name, description, value, person_id)
        return {"success": "updated person"}
    except:
        return {"error": "error updating person"}

@app.route('/attributes/<int:id>', methods=['DELETE'])
def delete_attribute(id):
    try:
        return db_delete_attribute(id)
    except:
        return {"error": "no such attribute"}


if __name__ == "__main__":
    app.run()
