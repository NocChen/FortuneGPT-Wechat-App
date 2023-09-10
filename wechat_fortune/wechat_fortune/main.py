## main.py
from flask import Flask, request, jsonify
from prediction import Prediction
from notification import Notification
from history import User

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'wechat_id' not in data or 'name' not in data or 'birth_date' not in data:
        return jsonify({'message': 'Bad Request'}), 400
    user = User(data['wechat_id'], data['name'], data['birth_date'])
    return jsonify({'message': 'User created'}), 200

@app.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.get_json()
    if not data or 'date' not in data or 'prediction' not in data or 'wechat_id' not in data:
        return jsonify({'message': 'Bad Request'}), 400
    prediction = Prediction(data['date'], data['prediction'])
    user = User.get_user(data['wechat_id'])
    if not user:
        return jsonify({'message': 'User not found'}), 404
    user.add_to_history(prediction)
    return jsonify({'message': 'Prediction created'}), 200

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.get_json()
    if not data or 'wechat_id' not in data or 'message' not in data:
        return jsonify({'message': 'Bad Request'}), 400
    notification = Notification(data['wechat_id'], data['message'])
    notification.send()
    return jsonify({'message': 'Notification sent'}), 200

if __name__ == '__main__':
    app.run(debug=True)

