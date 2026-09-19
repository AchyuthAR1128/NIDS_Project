# Network Intrusion Detection System using Machine Learning and Deep Learning Techniques

## Overview

This project presents a web based Network Intrusion Detection System that detects and classifies malicious network traffic using machine learning techniques. The system is built using the CICIDS2017 dataset and is capable of identifying multiple types of cyber attacks.

The aim of this project is to develop an efficient and practical solution that can distinguish between normal and malicious network behavior and further classify the type of attack.

---

## Features

- User login and registration system  
- Manual input based prediction  
- CSV file upload for batch prediction  
- Multiple machine learning models implemented  
- Stacking ensemble model for improved accuracy  
- Multi class attack classification  
- Web application built using Flask  

---

## Technologies Used

- Python  
- Flask  
- Pandas  
- NumPy  
- Scikit-learn  
- TensorFlow and Keras  
- MySQL  
- HTML and CSS  

---

## Dataset

The system is trained using the CICIDS2017 dataset, which represents realistic network traffic containing both normal and attack scenarios. It includes various types of attacks such as:

- Denial of Service  
- Port Scan  
- Brute Force  
- Web Attacks  
- Probe attacks  

The dataset provides detailed flow based features including packet statistics, flow duration, and protocol information.

---

## Project Workflow

1. Data Collection  
   Network traffic data is obtained from the CICIDS2017 dataset.

2. Data Preprocessing  
   - Handling missing values  
   - Feature selection  
   - Data normalization  
   - Label encoding  

3. Model Training  
   Multiple machine learning models are trained, including:
   - Decision Tree  
   - Random Forest  
   - K Nearest Neighbors  
   - Logistic Regression  
   - Naive Bayes  
   - CatBoost  

4. Ensemble Learning  
   A stacking ensemble model is used to combine predictions from multiple models to improve accuracy and reduce false positives.

5. Deployment  
   The trained model is saved and integrated into a Flask web application for real time prediction.

---

## System Architecture

Dataset → Preprocessing → Algorithms → Trained Model → User Interface → Prediction Output

The system uses machine learning, deep learning, and ensemble techniques for intrusion detection.

---

## Input Methods

- Manual Input  
  Users can enter feature values manually through the web interface.

- File Upload  
  Users can upload CSV files for batch prediction.

---

## Output

The system classifies network traffic as:

- Normal (Benign)  
- Attack  

If classified as an attack, it further identifies the type, such as:

- DoS  
- Port Scan  
- Probe  
- Brute Force  
- Web Attack XSS  

---

## Limitations

- Preprocessing pipeline is not fully integrated into deployment  
- Model depends on exact feature format  
- Deep learning models are not integrated into the web application  
- Real time traffic capture is not implemented  

---

## Future Scope

- Integrate preprocessing pipeline into deployment  
- Deploy deep learning models in real time system  
- Add real time network monitoring  
- Improve user interface and visualization  
- Enhance model performance using advanced techniques  

---

## Conclusion

This project demonstrates the application of machine learning techniques for detecting network intrusions. The stacking ensemble model improves detection accuracy and provides reliable classification of network traffic. The system can be extended further for real world deployment and advanced threat detection.

---
##Note
“Make sure MySQL server is running before starting the application”

---
