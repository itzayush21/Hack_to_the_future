from flask import Flask, jsonify, render_template
from algo import predict
app = Flask(__name__)

# Initialize SQLAlchemy with the Flask app


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("/index.html")


@app.route('/survey')
def survey():
    return render_template('survey.html')


@app.route('/info', methods=['GET', 'POST'])
def info():
    gender_mapping = {'Male': 0, 'Female': 1}
    sleep_quality_mapping = {'Good': 0, 'Poor': 1, 'Average': 2}
    stress_level_mapping = {'Low': 0, 'High': 1, 'Medium': 2}
    activity_level_mapping = {'Sedentary': 0, 'Active': 1}
    exercise_type_mapping = {'None': 0, 'Strength Training': 1, 'Cardio': 2}
    smoking_habits_mapping = {'Regular smoker': 0,
                              'Non-smoker': 1, 'Occasional smoker': 2}

    if request.method == 'POST':
        # Accessing form data
        age = request.form.get('age')
        gender = request.form.get('gender')
        height_cm = request.form.get('height_cm')
        weight_kg = request.form.get('weight_kg')
        sleep_hours = request.form.get('sleep_hours')
        sleep_quality = request.form.get('sleep_quality')
        stress_level = request.form.get('stress_level')
        work_type = request.form.get('work_type')
        alcohol_consumption = request.form.get('alcohol_consumption')
        smoking_habits = request.form.get('smoking_habits')
        daily_caloric_intake = request.form.get('daily_caloric_intake')
        protein_intake_g = request.form.get('protein_intake_g')
        carb_intake_g = request.form.get('carb_intake_g')
        fat_intake_g = request.form.get('fat_intake_g')
        fruit_veg_intake = request.form.get('fruit_veg_intake')
        daily_steps = request.form.get('daily_steps')
        exercise_type = request.form.get('exercise_type')
        exercise_duration_min = request.form.get('exercise_duration_min')
        heart_rate_bpm = request.form.get('heart_rate_bpm')
        blood_pressure_systolic = request.form.get('blood_pressure_systolic')
        blood_pressure_diastolic = request.form.get('blood_pressure_diastolic')
        blood_sugar_mg_dl = request.form.get('blood_sugar_mg_dl')
        cholesterol_mg_dl = request.form.get('cholesterol_mg_dl')
        liver_function_ast = request.form.get('liver_function_ast')
        liver_function_alt = request.form.get('liver_function_alt')
        mental_health_score = request.form.get('mental_health_score')
        bmi = request.form.get('bmi')

        numeric_gender = gender_mapping[gender]
        numeric_sleep_quality = sleep_quality_mapping[sleep_quality]
        numeric_stress_level = stress_level_mapping[stress_level]
        numeric_activity_level = activity_level_mapping[activity_level]
        numeric_exercise_type = exercise_type_mapping[exercise_type]
        numeric_smoking_habits = smoking_habits_mapping[smoking_habits]

        values_array = [age,
                        numeric_gender,
                        height_cm,
                        weight_kg,
                        sleep_hours,
                        numeric_sleep_quality,
                        numeric_stress_level,
                        numeric_activity_level,
                        alcohol_consumption,
                        numeric_smoking_habits,
                        daily_caloric_intake,
                        protein_intake_g,
                        carb_intake_g,
                        fat_intake_g,
                        fruit_veg_intake,
                        daily_steps,
                        numeric_exercise_type,
                        exercise_duration_min,
                        heart_rate_bpm,
                        blood_pressure_systolic,
                        blood_pressure_diastolic,
                        blood_sugar_mg_dl,
                        cholesterol_mg_dl,
                        liver_function_ast,
                        liver_function_alt,
                        mental_health_score,
                        bmi
                        ]

        # s=predict(values_array)We are going to send precaution,medicine etc here during full development

    return render_template('survey.html')


if __name__ == '__main__':
    app.run(debug=True)
