from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import euclidean_distances

app = Flask(__name__)

df = pd.read_csv("data/healthy_eating_dataset.csv")



kmeans = joblib.load("Model/kmeans.lb")
scaler = joblib.load("Model/scaler.lb")
le_cuisine = joblib.load("Model/le_cuisine.lb")
le_meal = joblib.load("Model/le_meal.lb")
le_diet = joblib.load("Model/le_diet.lb")

# Encode categorical columns
df["cuisine_encoded"] = le_cuisine.transform(df["cuisine"])
df["meal_encoded"] = le_meal.transform(df["meal_type"])
df["diet_encoded"] = le_diet.transform(df["diet_type"])

features = [
    "calories",
    "protein_g",
    "carbs_g",
    "fat_g",
    "fiber_g",
    "sugar_g",
    "sodium_mg",
    "cholesterol_mg",
    "serving_size_g",
    "cuisine_encoded",
    "meal_encoded",
    "diet_encoded"
]

X = df[features]

X_scaled = scaler.transform(X)

df["Cluster"] = kmeans.predict(X_scaled)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/recommend", methods=["POST"])
def recommend():

    # ---------- User Inputs ----------
    calories = float(request.form["calories"])
    protein = float(request.form["protein"])
    carbs = float(request.form["carbs"])
    fat = float(request.form["fat"])
    fiber = float(request.form["fiber"])
    sugar = float(request.form["sugar"])
    sodium = float(request.form["sodium"])
    cholesterol = float(request.form["cholesterol"])
    serving = float(request.form["serving"])

    cuisine = request.form["cuisine"]
    meal_type = request.form["meal_type"]
    diet_type = request.form["diet_type"]

    # ---------- Encode ----------
    cuisine_encoded = le_cuisine.transform([cuisine])[0]
    meal_encoded = le_meal.transform([meal_type])[0]
    diet_encoded = le_diet.transform([diet_type])[0]

    # ---------- Create User Input ----------
    user_input = np.array([[
        calories,
        protein,
        carbs,
        fat,
        fiber,
        sugar,
        sodium,
        cholesterol,
        serving,
        cuisine_encoded,
        meal_encoded,
        diet_encoded
    ]])

    # ---------- Scale ----------
    user_scaled = scaler.transform(user_input)

    # ---------- Predict Cluster ----------
    cluster = kmeans.predict(user_scaled)[0]

    # ---------- Get Meals ----------
    cluster_meals = df[df["Cluster"] == cluster].copy()

    # ---------- Calculate Distance ----------
    cluster_scaled = scaler.transform(cluster_meals[features])

    distances = euclidean_distances(user_scaled, cluster_scaled)

    cluster_meals["Distance"] = distances[0]

    # ---------- Sort ----------
    recommendations = cluster_meals.sort_values("Distance").head(6)

    return render_template(
        "result.html",
        meals=recommendations.to_dict(orient="records")
    )
        
if __name__ == "__main__":
    app.run(debug=True)