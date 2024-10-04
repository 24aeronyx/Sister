from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/request', methods=['POST'])
def request_response():
    data = request.json
    # Proses data
    response_data = {'message': f"Hello {data['name']}!"}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=5000)
