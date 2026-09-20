import os
from socket import herror
import cv2
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, flash, redirect, url_for
from Database import *
import pickle


app = Flask(__name__)

global filename
filename = ""

app.secret_key = os.environ.get('SECRET_KEY', 'development-secret-key')
app.config['SESSION_TYPE'] = 'filesystem'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html", xx= -1)

@app.route('/dashboard')
def dashboard():
   return render_template('dashboard.html', xx= -1)

@app.route('/index')
def index1():
   return render_template('index.html')


@app.route('/home')
def home():
   return render_template('index.html')


@app.route('/aboutme')
def aboutme():
   return render_template('aboutme.html')

@app.route('/register',methods = ['POST','GET'])
def registration():
	if request.method=="POST":
		username = request.form["username"]
		email = request.form["email"]
		password = request.form["password"]
		mobile = 0
		InsertData(username,email,password,mobile)
		return render_template('login.html')
		
	return render_template('register.html')


@app.route('/login',methods = ['POST','GET'])
def login():
   if request.method=="POST":
        email = request.form['email']
        passw = request.form['password']
        resp = read_cred(email, passw)
        if resp != None:
            return redirect("/dashboard")
        else:
            message = "Username and/or Password incorrect.\\n        Yo have not registered Yet \\nGo to Register page and do Registration";
            return "<script type='text/javascript'>alert('{}');</script>".format(message)

   return render_template('login.html')


# {'Dos': 0, 'Probe': 1, 'R2L': 2, 'U2R': 3, 'normal': 4}
def decode(output):
    print(output)
    if output ==0:
        return 'Dos Attack Found in Packet'
    elif output ==1:
        return 'Probe Attack Found in Packet'
    elif output ==2:
        return 'R2L Attack Found in Packet'
    elif output ==3:
        return 'U2R Attack Found in Packet'
    elif output ==4:
        return 'Normal Packet'


import pickle
import os
path = os.getcwd()
# loaded_model = pickle.load(open(path+"\\models\\rf_classifier.pkl", 'rb'))
## import joblib
import pandas as pd
import joblib

# Load the model from the file
model_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'StackingEnsemble.joblib')
loaded_model = joblib.load(model_filename)


# Reverse mapping dictionary to decode predicted class
class_mapping_reverse = {
    0: 'BENIGN',
    1: 'Bot',
    2: 'DDoS',
    3: 'DoS GoldenEye',
    4: 'DoS Hulk',
    5: 'DoS Slowhttptest',
    6: 'DoS slowloris',
    7: 'FTP-Patator',
    8: 'Heartbleed',
    9: 'Infiltration',
    10: 'PortScan',
    11: 'SSH-Patator',
    12: 'Web Attack � Brute Force',
    13: 'Web Attack � Sql Injection',
    14: 'Web Attack � XSS'
}

# Define the order and types of features manually
feature_order = [
    ' Fwd Packet Length Mean',
    ' Fwd Packet Length Max',
    ' Avg Fwd Segment Size',
    ' Subflow Fwd Bytes',
    'Total Length of Fwd Packets',
    ' Flow IAT Max',
    ' Average Packet Size',
    ' Bwd Packet Length Std',
    ' Flow Duration',
    ' Avg Bwd Segment Size',
    ' Bwd Packets/s', 
    ' Packet Length Mean',
    'Init_Win_bytes_forward',
    ' Init_Win_bytes_backward',
    ' Packet Length Std',
    ' Fwd IAT Max',
    ' Fwd Packet Length Std',
    ' Packet Length Variance',
    ' Total Length of Bwd Packets',
    ' Flow Packets/s'
]

SAMPLE_FILES = {
    'first': 'first_x_10_row_df.csv',
    'middle': 'middle_x_10_rows.csv',
    'last': 'last_x_10_rows.csv'
}

def preprocess_user_input(user_input):
    # Convert input to the appropriate data types
    for column in feature_order:
        user_input[column] = float(user_input[column]) 
    return pd.DataFrame([user_input])



# @app.route("/predict", methods=["GET", "POST"])
# def predict():
     
	 
# 	global filename
# 	if request.method == "POST":
          
# 		data = request.json	
# 		print(data)
# 		user_data = preprocess_user_input(data)
# 		print(user_data)
# 		prediction = loaded_model.predict(user_data)
# 		decoded_class = class_mapping_reverse.get(prediction[0], 'Unknown')

# 		# Print the decoded class
# 		print(f"The predicted class is: {decoded_class}")

# 		# Print the prediction
# 		print(f"The predicted class is: {prediction[0]}")

		# duration  = request.form["duration"]
		# protocol_type  = request.form["protocol_type"]
		# service  = request.form["service"]
		# flag  = request.form["flag"]
		# src_bytes  = request.form["src_bytes"]
		# dst_bytes  = request.form["dst_bytes"]
		# land  = request.form["land"]
		# wrong_fragment  = request.form["wrong_fragment"]
		# urgent  = request.form["urgent"]
		# hot  = request.form["hot"]
		# num_failed_logins  = request.form["num_failed_logins"]
		# logged_in  = request.form["logged_in"]
		# num_compromised  = request.form["num_compromised"]
		# root_shell  = request.form["root_shell"]
		# su_attempted  = request.form["su_attempted"]
		# num_file_creations  = request.form["num_file_creations"]
		# num_shells  = request.form["num_shells"]
		# num_access_files  = request.form["num_access_files"]
		# num_outbound_cmds  = request.form["num_outbound_cmds"]
		# is_host_login  = request.form["is_host_login"]
		# is_guest_login  = request.form["is_guest_login"]
		# count  = request.form["count"]
		# srv_count  = request.form["srv_count"]
		# serror_rate  = request.form["serror_rate"]
		# rerror_rate  = request.form["rerror_rate"]
		# same_srv_rate  = request.form["same_srv_rate"]
		# diff_srv_rate  = request.form["diff_srv_rate"]

		# print('\nduration:', duration,'\nprotocol_type:', protocol_type,'\nservice:', service,'\nflag:', flag,'\nsrc_bytes:', src_bytes,'\ndst_bytes:', dst_bytes,'\nland:', land,'\nwrong_fragment:', wrong_fragment,'\nurgent:', urgent,'\nhot:', hot,'\nnum_failed_logins:', num_failed_logins,'\nlogged_in:', logged_in,'\nnum_compromised:', num_compromised,'\nroot_shell:', root_shell,'\nsu_attempted:', su_attempted,'\nnum_file_creations:', num_file_creations,'\nnum_shells:', num_shells,'\nnum_access_files:', num_access_files,'\nnum_outbound_cmds:', num_outbound_cmds,'\nis_host_login:', is_host_login,'\nis_guest_login:', is_guest_login,'\ncount:', count,'\nsrv_count:', srv_count,'\nserror_rate:', serror_rate,'\nrerror_rate:', rerror_rate,'\nsame_srv_rate:', same_srv_rate,'\ndiff_srv_rate:', diff_srv_rate)
		
		# print("\n************************************************************")
		# input_data = []
		# input_data.append(float(duration))
		# input_data.append(int(protocol_type))
		# input_data.append(int(service))
		# input_data.append(int(flag))
		# input_data.append(float(src_bytes))
		# input_data.append(float(dst_bytes))
		# input_data.append(float(land))
		# input_data.append(float(wrong_fragment))
		# input_data.append(float(urgent))
		# input_data.append(float(hot))
		# input_data.append(float(num_failed_logins))
		# input_data.append(float(logged_in))
		# input_data.append(float(num_compromised))
		# input_data.append(float(root_shell))
		# input_data.append(float(su_attempted))
		# input_data.append(float(num_file_creations))
		# input_data.append(float(num_shells))
		# input_data.append(float(num_access_files))
		# input_data.append(float(num_outbound_cmds))
		# input_data.append(float(is_host_login))
		# input_data.append(float(is_guest_login))
		# input_data.append(float(count))
		# input_data.append(float(srv_count))
		# input_data.append(float(serror_rate))
		# input_data.append(float(rerror_rate))
		# input_data.append(float(same_srv_rate))
		# input_data.append(float(diff_srv_rate))

		# attack_type = decode(loaded_model.predict([input_data])[0])
		# print("\n**************** RESULT *********************\n")
		# print('Attack Type Resut = ',attack_type)

		# if attack_type=="Normal Packet":
		# 	return render_template("dashboard.html",attack=attack_type,safe='yes')
		# else:
		# 	return render_template("dashboard.html",attack=attack_type)


from flask import Flask, request, jsonify


@app.route("/predict", methods=["POST"])
def predict():
    try:	
        user_input = {}
        for column in feature_order:
            user_input[column] = request.form.get(column)

        print(user_input)
        # Preprocess user input
        user_data = pd.DataFrame([user_input])
 
        # Replace with your actual prediction logic
        prediction = loaded_model.predict(user_data)

        # Print the prediction
        print(f"The predicted class is: {prediction[0]}")
        decoded_class = class_mapping_reverse.get(prediction[0], 'Unknown')

        return render_template("dashboard.html",attack=decoded_class)


    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            sample_name = request.form.get('sample')
            if sample_name:
                sample_file = SAMPLE_FILES.get(sample_name)
                if sample_file is None:
                    return render_template('upload.html', error='Invalid sample CSV selected')
                sample_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test data', sample_file)
                if not os.path.isfile(sample_path):
                    return render_template('upload.html', error='The selected sample CSV is unavailable')
                df = pd.read_csv(sample_path)
            else:
                if 'file' not in request.files:
                    return render_template('upload.html', error='No file part')

                file = request.files['file']
                if file.filename == '':
                    return render_template('upload.html', error='No selected file')
                df = pd.read_csv(file)

            predictions = loaded_model.predict(df)
            class_names = [class_mapping_reverse.get(prediction, 'Unknown') for prediction in predictions]
            predictions = predictions.astype(np.int64).tolist()
            response = [{'sr_no': i+1, 'class_index': prediction, 'class_name': class_name} for i, (prediction, class_name) in enumerate(zip(predictions, class_names))]

            return render_template('upload.html', predictions=response)
        except Exception as e:
            if request.form.get('sample'):
                return render_template('upload.html', error='Unable to process the selected sample CSV')
            return render_template('upload.html', error=str(e))

    return render_template('upload.html', error=None)



if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )
