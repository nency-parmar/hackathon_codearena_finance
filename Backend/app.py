from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/suggest_budget', methods=['POST'])
def suggest_budget():
    data = request.get_json()
    goal_amount = float(data['goal_amount'])
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')

    # Calculate total months between dates
    months = max(1, (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month) + 1)
    monthly_saving = round(goal_amount / months, 2)

    return jsonify({'monthly_saving': monthly_saving})

if __name__ == '__main__':
    app.run(debug=True)