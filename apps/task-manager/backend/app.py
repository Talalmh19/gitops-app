from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://mongodb:27017/')
client = MongoClient(mongo_uri)
db = client['taskdb']
tasks_collection = db['tasks']

@app.route('/')
def home():
    return jsonify({"message": "Backend API is running!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find({}))
    # Convert ObjectId to string for JSON serialization
    for task in tasks:
        task['_id'] = str(task['_id'])
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    result = tasks_collection.insert_one(task)
    return jsonify({"message": "Task added", "id": str(result.inserted_id)}), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        task_data = request.json
        tasks_collection.update_one(
            {'_id': ObjectId(task_id)},
            {'$set': {'title': task_data['title']}}
        )
        return jsonify({"message": "Task updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        tasks_collection.delete_one({'_id': ObjectId(task_id)})
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
