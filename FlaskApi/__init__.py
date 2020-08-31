print('Starting flask api ...')
from flask import Flask,jsonify

flaskApi = Flask(__name__)

users = [
    {
        'id':1,
        'name':'Abhijit',
        'salary':12000
    },
    {
        'id':2,
        'name':'Santanu',
        'salary':13000
    }
]

@flaskApi.route('/api/getuser/<int:userid>', methods=['GET'])
def getUser(userid):
    user = [user for user in users
            if user['id'] == userid
            ]
    if len(user) == 0:
        return "No User found"
    return jsonify({'user':user[0]})

@flaskApi.route('/api/getAll', methods=['GET'])
def getAllUser():

    return jsonify({'users':users})


if __name__ == '__main__':
    flaskApi.run(debug=False)