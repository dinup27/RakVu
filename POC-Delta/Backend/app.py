from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/nodes')
def get_node_status():
    nodes = [
        {"name": "Node 1", "status": "Online", "cpu": "30%", "memory": "60%"},
        {"name": "Node 2", "status": "Offline", "cpu": "N/A", "memory": "N/A"},
        {"name": "Node 3", "status": "Online", "cpu": "70%", "memory": "85%"}
    ]
    return jsonify(nodes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)