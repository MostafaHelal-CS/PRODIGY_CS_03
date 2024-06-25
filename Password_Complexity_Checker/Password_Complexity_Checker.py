import re
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    # Criteria weights
    length_weight = 1.0
    upper_weight = 0.5
    digit_weight = 0.5
    special_weight = 0.5
    
    # Calculate criteria satisfaction
    length_score = len(password) * length_weight
    upper_score = len(re.findall(r'[A-Z]', password)) * upper_weight
    digit_score = len(re.findall(r'[0-9]', password)) * digit_weight
    special_score = len(re.findall(r'[\W_]', password)) * special_weight
    
    # Total score
    total_score = length_score + upper_score + digit_score + special_score
    
    # Determine password strength
    if total_score >= 20:
        strength = "Very Strong"
    elif total_score >= 15:
        strength = "Strong"
    elif total_score >= 10:
        strength = "Moderate"
    elif total_score >= 8:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Provide feedback
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should include at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should include at least one number.")
    if not re.search(r'[\W_]', password):
        feedback.append("Password should include at least one special character.")
    
    return {
        "strength": strength,
        "total_score": total_score,
        "feedback": feedback
    }

def check_password():
    password = entry.get()
    assessment = assess_password_strength(password)
    result = f"Password Strength: {assessment['strength']}\n"
    result += f"Total Score: {assessment['total_score']}\n"
    result += "Feedback:\n"
    for comment in assessment['feedback']:
        result += f"- {comment}\n"
    messagebox.showinfo("Password Assessment", result)

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")


frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Enter a password:", bg='#f0f0f0',font=("Cursive", 13, "bold"))
label.pack(pady=5)

entry = tk.Entry(frame, width=30,font=("Cursive", 12, "bold"))
entry.pack(pady=5)

check_button = tk.Button(frame, text="Check Strength", command=check_password,background="green",foreground="white",font=("Cursive", 13, "bold"))
check_button.pack(pady=10,padx=10)

# Start the GUI event loop
root.mainloop()
