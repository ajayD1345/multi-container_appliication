from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def data():
    return jsonify({"message": "Hello from the backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
