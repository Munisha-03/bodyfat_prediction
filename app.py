# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)

# with open('rfc_bodyfat.pkl', 'rb') as f:
#     model = pickle.load(f)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         try:
#             # Fetch form data and handle missing fields
#             weight = request.form.get('weight')
#             neck = request.form.get('neck')
#             chest = request.form.get('chest')
#             abdomen = request.form.get('abdomen')
#             hip = request.form.get('hip')
#             thigh = request.form.get('thigh')
#             knee = request.form.get('knee')
#             bicep = request.form.get('bicep')
#             forearm = request.form.get('forearm')
#             wrist = request.form.get('wrist')
            
#             # Check if any field is missing
#             if None in (weight, neck, chest, abdomen, hip, thigh, knee, bicep, forearm, wrist):
#                 return render_template('predict.html', res="Please fill out all fields.")

#             # Convert to float and handle conversion errors
#             weight = float(weight)
#             neck = float(neck)
#             chest = float(chest)
#             abdomen = float(abdomen)
#             hip = float(hip)
#             thigh = float(thigh)
#             knee = float(knee)
#             bicep = float(bicep)
#             forearm = float(forearm)
#             wrist = float(wrist)

#             # Prepare input for prediction
#             input_data = [weight, neck, chest, abdomen, hip, thigh, knee, bicep, forearm, wrist]
#             predicted_bodyfat = model.predict([input_data])[0]

#             return render_template('predict.html', res=f"Predicted Body Fat Percentage: {predicted_bodyfat:.2f}")

#         except ValueError:
#             return render_template('predict.html', res="Invalid input. Please enter numerical values.")

#     # For GET request, just render the predict page
#     return render_template('predict.html', res="")

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('rfc_bodyfat.pkl', 'rb') as f:
    model = pickle.load(f)            

@app.route('/')  
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        try:
            weight = request.form.get('weight')
            neck = request.form.get('neck')
            chest = request.form.get('chest')
            abdomen = request.form.get('abdomen')
            hip = request.form.get('hip')
            thigh = request.form.get('thigh')
            knee = request.form.get('knee')
            bicep = request.form.get('bicep')
            forearm = request.form.get('forearm')
            wrist = request.form.get('wrist')

            if None in (weight, neck, chest, abdomen, hip, thigh, knee, bicep, forearm, wrist):
                return render_template('result.html', res="Please fill out all fields.")

            input=[weight, neck, chest, abdomen, hip, thigh, knee, bicep, forearm, wrist] 

            predicted_bodyfat = model.predict([input])[0]

            return render_template('result.html', res=f"Predicted Body Fat Percentage: {predicted_bodyfat:.2f}")

        except ValueError:
            return render_template('predict.html', res="Invalid input. Please enter numerical values.")

     # For GET request, just render the predict page
    return render_template('result.html', res="")

if __name__ == '__main__':
    app.run(debug=True)
