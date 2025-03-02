from flask import Flask, jsonify
from system_info import get_system_info

app = Flask(__name__)

@app.route('/api/system-info', methods=['GET'])
def system_info():
    try:
        info = get_system_info()
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)