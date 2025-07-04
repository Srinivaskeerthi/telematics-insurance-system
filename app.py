from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest_data():
    data = request.json
    # Simple validation
    if not data or 'speed' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    # For prototype: save data to a file or queue (here just print)
    print("Received data:", data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(port=5000)
    