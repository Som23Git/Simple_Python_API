from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'title': u'Buy Products',
        'description': u'Need to buy a good product from the web',
        'done': False
    },
    {
        'id': 4,
        'title': u'Buy Electronics',
        'description': u'Get new electronics from the web',
        'done': False
    },
    {
        'id': 5,
        'title': u'Database',
        'description': u'Update a New Database',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)