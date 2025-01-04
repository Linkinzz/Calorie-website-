from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add-food', methods=['POST'])
def add_food():
    data = request.json
    food_name = data['foodName']
    portion = float(data['portion'])

    # Mock calorie data
    calorie_data = {"apple": 52, "banana": 89, "bread": 265}
    calories_per_100g = calorie_data.get(food_name.lower(), 0)
    total_calories = (calories_per_100g / 100) * portion

    return jsonify({'totalCalories': total_calories})

if __name__ == '__main__':
    app.run(debug=True)
