Branch Recommendation System
A simple machine learning-based web application that predicts the most suitable engineering branch for a student based on their academic scores and reservation category. This project simulates the branch allocation process used in many Indian engineering colleges.

Project Overview
In Indian engineering admissions, branch allocation is often based on academic performance in 10th and 12th (PUC) along with the student's reservation category (General, OBC, SC, ST). This project uses a trained Random Forest Classifier to recommend one of the following engineering branches:

Computer Science Engineering (CSE)

Electronics and Communication Engineering (ECE)

Electrical and Electronics Engineering (EEE)

Civil Engineering

Mechanical Engineering (MECH)

How It Works
The user provides the following inputs:

10th CGPA

PUC CGPA

Caste Category (General / OBC / SC / ST)

The input data is preprocessed and encoded.

The encoded data is passed to a pre-trained machine learning model (RandomForestClassifier).

The model predicts the most suitable engineering branch based on historical data patterns.

Features
Takes user input from a React frontend.

Sends input to a FastAPI backend for processing.

Uses a trained machine learning model for prediction.

Displays the recommended engineering branch instantly.

Clean UI with real-time communication between frontend and backend.

Tech Stack
Python: Core programming language for backend and machine learning logic.

Scikit-learn: Model training and evaluation using Random Forest.

Pandas: For dataset manipulation and preprocessing.

Pickle: To serialize and deserialize the model and encoders.

FastAPI: Backend API server to serve the ML model predictions.

React with Vite: Modern frontend to collect and send user input.

