import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import joblib

# Load trained model and scaler
model = joblib.load("logistic_regression.pkl")
scaler = joblib.load("scaler.pkl")

# Function to predict cancer
def predict():
    try:
        input_values = [float(entry.get()) for entry in entries]

        # Convert input to DataFrame with feature names
        input_data = pd.DataFrame([input_values], columns=scaler.feature_names_in_)

        # Normalize using the saved scaler
        input_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_data)[0]

        # Show result
        result_text = "Benign (No Cancer)" if prediction == 1 else "Malignant (Cancer Detected)"
        result_label.config(text=f"Diagnosis: {result_text}", fg="green" if prediction == 1 else "red")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create Tkinter window
root = tk.Tk()
root.title("Breast Cancer Diagnosis")
root.geometry("600x500")

# Split features into two columns
labels = scaler.feature_names_in_
entries = []
frame = tk.Frame(root)
frame.pack(pady=20)

left_frame = tk.Frame(frame)
left_frame.pack(side="left", padx=20)

right_frame = tk.Frame(frame)
right_frame.pack(side="right", padx=20)

# Add entry fields to left and right columns
for i in range(len(labels)):
    parent = left_frame if i < len(labels) / 2 else right_frame
    row = tk.Frame(parent)
    row.pack(fill="x", pady=5)

    tk.Label(row, text=f"{labels[i]}:").pack(side="left")
    entry = tk.Entry(row, width=10)
    entry.pack(side="right")
    entries.append(entry)

# Predict button (Centered)
predict_button = tk.Button(root, text="Predict", command=predict, font=("Arial", 12), bg="blue", fg="white")
predict_button.pack(pady=20)

# Result Label (Centered)
result_label = tk.Label(root, text="Diagnosis: -", font=("Arial", 14, "bold"))
result_label.pack()

# Run GUI
root.mainloop()

