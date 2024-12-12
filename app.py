from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Health Metrics API!"})

@app.route("/bmi", methods=["POST"])
def bmi():
    data = request.get_json()
    try:
        # Vérification des paramètres
        weight = data["weight"]
        height = data["height"]
        
        if height <= 0 or weight <= 0:
            return jsonify({"error": "Weight and height must be positive values"}), 400
        
        # Calcul du BMI
        bmi_value = calculate_bmi(weight, height)
        return jsonify({"operation": "BMI", "result": bmi_value})
    
    except KeyError:
        return jsonify({"error": "Missing required parameters 'weight' and 'height'"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/bmr", methods=["POST"])
def bmr():
    data = request.get_json()
    try:
        # Vérification des paramètres
        weight = data["weight"]
        height = data["height"]
        age = data["age"]
        gender = data["gender"]
        
        if height <= 0 or weight <= 0 or age <= 0:
            return jsonify({"error": "Weight, height, and age must be positive values"}), 400
        
        if gender not in ["male", "female"]:
            return jsonify({"error": "Gender must be either 'male' or 'female'"}), 400
        
        # Calcul du BMR
        bmr_value = calculate_bmr(weight, height, age, gender)
        return jsonify({"operation": "BMR", "result": bmr_value})
    
    except KeyError:
        return jsonify({"error": "Missing required parameters 'weight', 'height', 'age', and 'gender'"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")