import json

import flask
from flask import make_response, jsonify
from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()

conn = sqlite3.connect('/Users/dpavlovski/Desktop/paysafe-hackathon-vmv/Backend/Kidromeda.db')
c = conn.cursor()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
        conn = sqlite3.connect('/Users/dpavlovski/Desktop/paysafe-hackathon-vmv/Backend/Kidromeda.db')
        c = conn.cursor()
        query = "SELECT PASSWORD FROM Kid WHERE EMAIL = '" + username + "'"
        c.execute(query)
        password_db = c.fetchone()[0]
        if check_password_hash(password_db, password):
            return username



"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   Register kid (POST) parent id - 
        request-
        
        {
            "email": "VALUE",
            "password": "VALUE",
            "name": "VALUE"
        }
   
             response - 201
            
"""


@app.route('/parent/<int:id>/kid', methods=['POST'])
@auth.login_required
def register_kid(id):
    try:
        conn = sqlite3.connect('/Users/dpavlovski/Desktop/paysafe-hackathon-vmv/Backend/Kidromeda.db')
        c = conn.cursor()

        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')

        balance = 0
        parent_id = id

        c.execute("INSERT INTO Kid(NAME,Email,PASSWORD,BALANCE,Parent_id) VALUES (?, ?, ?, ?, ?)",
                  (name, email, generate_password_hash(password),balance,parent_id))
        conn.commit()

        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 201)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response



"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   Register parent (POST)  - 
               request -
        {
            "email": "VALUE",
            "password": "VALUE",
            "name": "VALUE"
        }

             response - 201
"""


@app.route('/parent', methods=['POST'])
@auth.login_required
def register_parent():
    try:
        conn = sqlite3.connect('/Users/dpavlovski/Desktop/paysafe-hackathon-vmv/Backend/Kidromeda.db')
        c = conn.cursor()

        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')

        c.execute("INSERT INTO Parent(NAME,Email,PASSWORD) VALUES (?, ?, ?)",
                  (name, email, generate_password_hash(password)))
        conn.commit()

        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 201)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response


"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   Register task (POST)      
        request -
                {
                    "summary": "VALUE",
                    "reward": "VALUE"
                }
                
              response - 201
"""


@app.route('/parent/<int:parent_id>/kid/<int:kid_id>/task', methods=['POST'])
@auth.login_required
def register_task():
    try:
        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 201)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response


"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   Login  (GET)  -
            

            response - 200
            {
                "is_parent": "VALUE",
                "name": "VALUE"
            }
"""


@app.route('/login', methods=['GET'])
@auth.login_required
def login_kid():
    try:
        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 200)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response


"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   parent/$ID?kids (GET) - 

          response - 
                    
{children: { name, balance, tasks: [{ summary, status, reward, image: string|null, comment: string }] }
"""


@app.route('/parent/<int:id>/kid', methods=['GET'])
@auth.login_required
def parent_ID_kids(id):
    try:
        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 200)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response



"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   Kid tasks (PUT) (kid ready method) - 
            {
                "image": "VALUE",
                "comment": "VALUE"
            }
    response - 201
"""


@app.route('/parent/<int:parent_id>/kid/<int:kid_id>/task/<int:task_id>', methods=['PUT'])
@auth.login_required
def kid_tasks_put():
    try:
        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 201)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response


"""
   AUTHORIZATION HEADER - EMAIL & PASSWORD
   Kid tasks (POST) (verify if the task is done) - 
            request-
            {
                "verify": "VALUE",
            }
            
            
      response - 200

"""


@app.route('/parent/<int:parent_id>/kid/<int:kid_id>/task/<int:task_id>/verify', methods=['POST'])
@auth.login_required
def parants_tasks_put():
    try:
        json_temp = "{}"
        temp_response = json.loads(json_temp)
        response = make_response(temp_response, 200)
        return response
    except:
        response = make_response(jsonify({"error": "Not found"}), 404)
        return response

