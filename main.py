from flask import Flask, jsonify, render_template, request
from algo import predict
from algo2 import predict1
app = Flask(__name__)

# Initialize SQLAlchemy with the Flask app
health_issues_recommendations = {
    'Obesity': {
        'Precaution': [
            'Regularly monitor weight.',
            'Avoid high-calorie foods.',
            'Practice portion control.'
        ],
        'Diet Plan': [
            'Focus on vegetables, lean proteins, whole grains.',
            'Avoid sugary drinks and high-fat foods.',
            'Maintain a caloric deficit.'
        ],
        'Medications (India)': [
            'Orlistat (Alli)',
            'Metformin (Glucophage)',
            'Lorcaserin (Belviq)'
        ],
        'Future Concerns': [
            'Risk of cardiovascular diseases.',
            'Increased risk of diabetes.',
            'Joint problems.'
        ],
        'Exercise Plan': [
            '150 minutes of moderate aerobic activity weekly (e.g., brisk walking, cycling).',
            'Strength training twice a week.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Obesity'
    },
    'Cardiac_Issue': {
        'Precaution': [
            'Regular heart health check-ups.',
            'Avoid excessive salt.',
            'Manage stress and quit smoking.'
        ],
        'Diet Plan': [
            'Fruits, vegetables, whole grains, lean proteins.',
            'Limit saturated fats, cholesterol.'
        ],
        'Medications (India)': [
            'Aspirin',
            'Statins (Atorvastatin)',
            'Beta-blockers (Metoprolol)'
        ],
        'Future Concerns': [
            'Risk of heart attack.',
            'Potential for stroke.',
            'Risk of heart failure.'
        ],
        'Exercise Plan': [
            'Low-impact exercises (e.g., walking, swimming).',
            '150 minutes of moderate-intensity exercise per week.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Cardiovascular_disease'
    },
    'Liver_Problem': {
        'Precaution': [
            'Avoid alcohol.',
            'Maintain a healthy weight.',
            'Regular liver function tests.'
        ],
        'Diet Plan': [
            'Balanced diet with fruits, vegetables, whole grains.',
            'Avoid fatty foods and limit sugar intake.'
        ],
        'Medications (India)': [
            'Ursodeoxycholic Acid (Ursofalk)',
            'Silymarin (Milk Thistle)',
            'Enalapril (Vasotec)'
        ],
        'Future Concerns': [
            'Risk of liver cirrhosis.',
            'Potential for liver failure.',
            'Risk of liver cancer.'
        ],
        'Exercise Plan': [
            'Moderate physical activity (e.g., walking, yoga).',
            'Focus on maintaining a healthy weight.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Liver_disease'
    },
    'Respiratory_Issue': {
        'Precaution': [
            'Avoid exposure to pollutants.',
            'Quit smoking.',
            'Get vaccinated against respiratory infections.'
        ],
        'Diet Plan': [
            'Foods rich in antioxidants (e.g., berries, nuts).',
            'Maintain proper hydration.'
        ],
        'Medications (India)': [
            'Salbutamol (Ventolin)',
            'Ipratropium (Atrovent)',
            'Montelukast (Singulair)'
        ],
        'Future Concerns': [
            'Risk of chronic obstructive pulmonary disease (COPD).',
            'Asthma exacerbations.',
            'Potential for respiratory infections.'
        ],
        'Exercise Plan': [
            'Low-impact exercises (e.g., walking, swimming).',
            'Breathing exercises and pulmonary rehabilitation.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Respiratory_disease'
    },
    'Nutritional_Deficiency': {
        'Precaution': [
            'Regularly monitor nutritional intake.',
            'Consider supplementation if necessary.'
        ],
        'Diet Plan': [
            'Balanced diet rich in vitamins and minerals.',
            'Include diverse food groups.'
        ],
        'Medications (India)': [
            'Vitamin Supplements (e.g., Vitamin D3, B12)',
            'Iron Supplements (e.g., Ferrous Sulfate)'
        ],
        'Future Concerns': [
            'Risk of anemia.',
            'Potential for weakened immune system.'
        ],
        'Exercise Plan': [
            'Moderate exercise to improve overall health.',
            'Focus on balanced nutrition rather than exercise alone.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Nutritional_deficiency'
    },
    'Mental_Health_Concern': {
        'Precaution': [
            'Regular mental health check-ups.',
            'Manage stress effectively.',
            'Seek professional help if needed.'
        ],
        'Diet Plan': [
            'Foods rich in omega-3 fatty acids (e.g., fish, flaxseeds).',
            'Include fruits, vegetables, and whole grains.'
        ],
        'Medications (India)': [
            'Antidepressants (e.g., Fluoxetine, Sertraline)',
            'Anxiolytics (e.g., Diazepam)'
        ],
        'Future Concerns': [
            'Risk of chronic mental health disorders.',
            'Potential for decreased quality of life.'
        ],
        'Exercise Plan': [
            'Regular physical activity to improve mood (e.g., walking, yoga).',
            'Consider relaxation techniques and mindfulness.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Mental_disorder'
    },
    'Hypertension': {
        'Precaution': [
            'Monitor blood pressure regularly.',
            'Reduce sodium intake.',
            'Manage stress.'
        ],
        'Diet Plan': [
            'Low-sodium diet.',
            'Include fruits, vegetables, and whole grains.'
        ],
        'Medications (India)': [
            'Antihypertensives (e.g., Amlodipine, Losartan)',
            'Diuretics (e.g., Hydrochlorothiazide)'
        ],
        'Future Concerns': [
            'Risk of heart disease.',
            'Potential for stroke.',
            'Kidney damage.'
        ],
        'Exercise Plan': [
            'Regular aerobic activity (e.g., walking, swimming).',
            'Strength training exercises.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Hypertension'
    },
    'Low_Physical_Activity': {
        'Precaution': [
            'Incorporate more movement into daily routine.',
            'Set realistic activity goals.'
        ],
        'Diet Plan': [
            'Balanced diet with moderate calorie intake.',
            'Include proteins, healthy fats, and fibers.'
        ],
        'Medications (India)': [
            'Generally not applicable unless related to a specific condition.'
        ],
        'Future Concerns': [
            'Risk of obesity.',
            'Potential for cardiovascular issues.'
        ],
        'Exercise Plan': [
            'Gradually increase physical activity.',
            'Include both aerobic and strength training exercises.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Physical_inactivity'
    },
    'High_Fat_Intake': {
        'Precaution': [
            'Monitor fat intake.',
            'Choose healthy fats (e.g., avocados, nuts).'
        ],
        'Diet Plan': [
            'Limit saturated and trans fats.',
            'Include healthy fats and fibers.'
        ],
        'Medications (India)': [
            'Statins (e.g., Atorvastatin)',
            'Omega-3 supplements'
        ],
        'Future Concerns': [
            'Risk of cardiovascular disease.',
            'Potential for weight gain.'
        ],
        'Exercise Plan': [
            'Regular physical activity.',
            'Focus on overall cardiovascular health.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/High-fat_diet'
    },
    'Diabetes': {
        'Precaution': [
            'Regular monitoring of blood glucose levels.',
            'Follow a diabetic-friendly diet.'
        ],
        'Diet Plan': [
            'Low glycemic index foods.',
            'Include whole grains, lean proteins, and vegetables.'
        ],
        'Medications (India)': [
            'Metformin (Glucophage)',
            'Insulin',
            'Sulfonylureas (e.g., Glibenclamide)'
        ],
        'Future Concerns': [
            'Risk of heart disease.',
            'Potential for neuropathy.'
        ],
        'Exercise Plan': [
            'Regular aerobic and strength training exercises.',
            'Focus on blood sugar control.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Diabetes_mellitus'
    },
    'Kidney_Problem': {
        'Precaution': [
            'Monitor kidney function regularly.',
            'Avoid excessive salt and protein intake.'
        ],
        'Diet Plan': [
            'Low-sodium, low-protein diet.',
            'Include fruits and vegetables.'
        ],
        'Medications (India)': [
            'Diuretics (e.g., Furosemide)',
            'ACE inhibitors (e.g., Ramipril)'
        ],
        'Future Concerns': [
            'Risk of kidney failure.',
            'Potential for fluid imbalances.'
        ],
        'Exercise Plan': [
            'Moderate physical activity.',
            'Avoid excessive strain.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Kidney_disease'
    },
    'Lack_of_Exercise': {
        'Precaution': [
            'Gradually increase physical activity.',
            'Set achievable exercise goals.'
        ],
        'Diet Plan': [
            'Balanced diet to support increased activity levels.',
            'Include a mix of proteins, carbs, and healthy fats.'
        ],
        'Medications (India)': [
            'Generally not applicable unless related to a specific condition.'
        ],
        'Future Concerns': [
            'Risk of obesity and cardiovascular issues.',
            'Potential for mental health concerns.'
        ],
        'Exercise Plan': [
            'Start with light exercises and gradually increase intensity.',
            'Include aerobic and strength training exercises.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Physical_inactivity'
    },
    'No_issue': {
        'Precaution': [
            'Maintain a healthy lifestyle.',
            'Regular health check-ups.'
        ],
        'Diet Plan': [
            'Balanced diet to support overall health.',
            'Include a variety of nutrients.'
        ],
        'Medications (India)': [
            'Generally not applicable.'
        ],
        'Future Concerns': [
            'Continue maintaining a healthy lifestyle.'
        ],
        'Exercise Plan': [
            'Regular physical activity.',
            'Maintain a balanced exercise routine.'
        ],
        'Article_Link': 'https://www.example.com/respiratory-issue-article'
    }
}


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("/index.html")


@app.route('/survey')
def survey():
    return render_template('survey.html')


def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # convert height to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi


@app.route('/info', methods=['GET', 'POST'])
def info():
    gender_mapping = {'Male': 0, 'Female': 1}
    sleep_quality_mapping = {'Good': 1, 'Poor': 2, 'Average': 0}
    stress_level_mapping = {'Low': 1, 'High': 0, 'Medium': 2}
    activity_level_mapping = {'Sedentary': 1, 'Active': 0}
    exercise_type_mapping = {'None': 1, 'Strength Training': 2, 'Cardio': 0}
    smoking_habits_mapping = {'Regular smoker': 2,
                              'Non-smoker': 0, 'Occasional smoker': 12}

    if request.method == 'POST':
        # Accessing form data
        age = request.form.get('age')
        gender = request.form.get('gender')
        height_cm = request.form.get('height_cm')
        weight_kg = request.form.get('weight_kg')
        sleep_hours = request.form.get('sleep_hours')
        sleep_quality = request.form.get('sleep_quality')
        stress_level = request.form.get('stress_level')
        activity_level = request.form.get('work_type')
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
        bmi = 27.1

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

    # We are going to send precaution, medicine etc here during full development
        s, issue, input = predict(values_array)
        return render_template('survey.html', input=input, issue=issue, result=health_issues_recommendations)
    return render_template('survey.html')
    # return render_template('survey.html')


@app.route('/symptom')
def symptom():
    return render_template('symptom.html')


disease_recommendations = {
    'Arthritis': {
        'Treatment': [
            'Consult a rheumatologist for a treatment plan.',
            'Use anti-inflammatory medications as prescribed.',
            'Engage in regular low-impact exercise to maintain joint flexibility.',
            'Apply heat or cold packs to affected joints for pain relief.'
        ],
        'Medical Advice': [
            'Consider physical therapy to strengthen muscles around joints.',
            'Maintain a healthy weight to reduce joint stress.',
            'Regularly follow up with your healthcare provider.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Arthritis'
    },
    'Cold': {
        'Treatment': [
            'Rest and drink plenty of fluids.',
            'Use over-the-counter cold medications to alleviate symptoms.',
            'Gargle with warm salt water for a sore throat.',
            'Use a humidifier to ease congestion.'
        ],
        'Medical Advice': [
            'Seek medical attention if symptoms persist beyond 10 days.',
            'Consult a doctor if you experience severe symptoms or complications.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Common_cold'
    },
    'Fatigue': {
        'Treatment': [
            'Ensure you get adequate sleep each night.',
            'Maintain a balanced diet and stay hydrated.',
            'Engage in regular physical activity to boost energy levels.',
            'Manage stress through relaxation techniques and hobbies.'
        ],
        'Medical Advice': [
            'Consult a healthcare provider if fatigue persists or worsens.',
            'Review any medications you are taking with your doctor as some may cause fatigue.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Fatigue_(medical)'
    },
    'Flu': {
        'Treatment': [
            'Rest and stay hydrated.',
            'Use antiviral medications if prescribed by a doctor.',
            'Manage fever and body aches with over-the-counter medications.',
            'Avoid contact with others to prevent spreading the flu.'
        ],
        'Medical Advice': [
            'Seek medical attention if you have difficulty breathing or chest pain.',
            'Consider getting a flu vaccine to prevent future occurrences.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Influenza'
    },
    'Heart Disease': {
        'Treatment': [
            'Follow a heart-healthy diet low in saturated fats and cholesterol.',
            'Engage in regular physical activity.',
            'Take medications as prescribed by your cardiologist.',
            'Monitor and manage blood pressure and cholesterol levels.'
        ],
        'Medical Advice': [
            'Regularly follow up with a cardiologist for ongoing management.',
            'Consider lifestyle changes such as quitting smoking and reducing alcohol intake.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Cardiovascular_disease'
    },
    'None': {
        'Treatment': [
            'Maintain a healthy lifestyle with balanced diet and regular exercise.',
            'Schedule regular check-ups with your healthcare provider.'
        ],
        'Medical Advice': [
            'Continue monitoring your health and be aware of any changes.',
            'Consult a healthcare provider if you develop any new symptoms.'
        ],
        'Article_Link': 'https://en.wikipedia.org/wiki/Respiratory_disease'
    },
    'Respiratory Issue': {
        'Treatment': [
            'Avoid allergens and irritants that trigger respiratory issues.',
            'Use prescribed inhalers or medications as directed.',
            'Practice good respiratory hygiene and avoid smoking.'
        ],
        'Medical Advice': [
            'Seek regular evaluations from a pulmonologist or allergist.',
            'Follow a treatment plan and avoid known triggers.'
        ],
        'Article_Link': 'https://example.com/respiratory-issue'
    }
}


@app.route('/info2', methods=['GET', 'POST'])
def info2():
    if request.method == 'POST':
        age = request.form.get('age', type=int)
        gender = request.form.get('gender')

        # Map gender to binary values
        gender_map = {'male': 1, 'female': 0}
        # Default to None if gender is not valid
        gender_value = gender_map.get(gender, None)

        # Retrieve symptoms and map to binary values
        symptoms = {
            'headache': 1 if request.form.get('headache') == 'Yes' else 0,
            'fever': 1 if request.form.get('fever') == 'Yes' else 0,
            'cough': 1 if request.form.get('cough') == 'Yes' else 0,
            'fatigue': 1 if request.form.get('fatigue') == 'Yes' else 0,
            'body_aches': 1 if request.form.get('body_aches') == 'Yes' else 0,
            'chest_pain': 1 if request.form.get('chest_pain') == 'Yes' else 0,
            'sore_throat': 1 if request.form.get('sore_throat') == 'Yes' else 0,
            'shortness_of_breath': 1 if request.form.get('shortness_of_breath') == 'Yes' else 0,
            'runny_nose': 1 if request.form.get('runny_nose') == 'Yes' else 0,
            'joint_pain': 1 if request.form.get('joint_pain') == 'Yes' else 0,
            'nausea': 1 if request.form.get('nausea') == 'Yes' else 0,
            'dizziness': 1 if request.form.get('dizziness') == 'Yes' else 0,
            'abdominal_pain': 1 if request.form.get('abdominal_pain') == 'Yes' else 0,
            'confusion': 1 if request.form.get('confusion') == 'Yes' else 0,
        }

        # Retrieve severity and map to numerical values
        severity = request.form.get('severity')
        severity_map = {'Mild': 1, 'Moderate': 2, 'Severe': 3}
        # Default to None if severity is not valid
        severity_value = severity_map.get(severity, None)

        # Collect all data into an array
        data_array = [
            age,
            gender_value,
            symptoms['headache'], symptoms['fever'], symptoms['cough'],
            symptoms['fatigue'], symptoms['body_aches'], symptoms['chest_pain'],
            symptoms['sore_throat'], symptoms['shortness_of_breath'],
            symptoms['runny_nose'], symptoms['joint_pain'], symptoms['nausea'],
            symptoms['dizziness'], symptoms['abdominal_pain'], symptoms['confusion'],
            severity_value
        ]
        s = predict1(data_array)

        return render_template('symptom.html', data=symptoms, s=s, res=disease_recommendations)
    return render_template('symptom.html')


if __name__ == '__main__':
    app.run(debug=True)

