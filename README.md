# 🥗 Nutrition Recommendation System

A **Machine Learning-based web application** that recommends the most suitable meals based on a user's nutritional requirements such as **Calories, Protein, Carbohydrates, Fat, Fiber, Sugar, Sodium, Cholesterol, and Serving Size**. The system uses the **K-Means Clustering** algorithm to group similar meals and recommends the closest matches using **Euclidean Distance**.

The project is developed using **Python, Flask, HTML, CSS, Pandas, NumPy, and Scikit-learn**.

---

# 📌 Features

- 🥗 Personalized meal recommendations using Machine Learning
- 🤖 K-Means Clustering based recommendation system
- 🍎 Nutrition-based food suggestions
- 🎯 User-friendly and responsive interface
- 📊 Displays Top 5 recommended meals
- 🍽 Complete nutritional information
- 🌍 Filter meals by Cuisine, Meal Type, and Diet Type
- ⚡ Fast recommendation results
- 🖥 Flask backend
- ✅ Input validation using HTML forms

---

# 📷 Project Preview

## 🏠 Home Page

- Modern Landing Page
- Nutrition Recommendation Overview
- Responsive Navigation Bar
- Attractive User Interface

---

## 🥗 Recommendation Page

- User Nutrition Input Form
- Cuisine Selection
- Meal Type Selection
- Diet Type Selection
- Generate Personalized Recommendations

---

## 🍽 Result Page

- Top Recommended Meals
- Meal Images
- Meal Name
- Calories
- Protein
- Carbohydrates
- Fat
- Fiber
- Sugar
- Sodium
- Cholesterol
- Serving Size
- Rating

---

# 🧠 Machine Learning Model

## Algorithm Used

### **K-Means Clustering**

The model groups meals based on their nutritional values and predicts the nearest cluster according to the user's nutritional requirements.

After clustering, **Euclidean Distance** is used to find the closest matching meals from the predicted cluster.

---

# 📊 Input Features

| Feature | Description |
|----------|-------------|
| Calories | Required Calories |
| Protein | Protein (g) |
| Carbohydrates | Carbohydrates (g) |
| Fat | Fat (g) |
| Fiber | Fiber (g) |
| Sugar | Sugar (g) |
| Sodium | Sodium (mg) |
| Cholesterol | Cholesterol (mg) |
| Serving Size | Serving Size (g) |
| Cuisine | Indian, American, Mexican, Thai, Mediterranean, etc. |
| Meal Type | Breakfast, Lunch, Dinner, Snack |
| Diet Type | Vegan, Vegetarian, Keto, Paleo, Balanced |

---

# 🎯 Output

The application recommends the **Top 5 similar meals** with complete nutritional information.

### Recommendation Includes

- Meal Name
- Cuisine
- Meal Type
- Diet Type
- Calories
- Protein
- Carbohydrates
- Fat
- Fiber
- Sugar
- Sodium
- Cholesterol
- Serving Size
- Cooking Method
- Rating

---

# 🛠 Technologies Used

## Frontend

- HTML
- CSS

## Backend

- Python
- Flask

## Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

---

# 📂 Project Structure

```text
Nutrition_Recommendation_System/
│
├── data/
│   └── healthy_eating_dataset.csv
│
├── Model/
│   ├── kmeans.lb
│   ├── scaler.lb
│   ├── le_cuisine.lb
│   ├── le_meal.lb
│   └── le_diet.lb
│
├── static/
│   ├── css/
│       └── style.css
│  
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── project.html
│   ├── result.html
│   └── contact.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Nutrition_Recommendation_System.git
```

---

## 2️⃣ Move to Project Folder

```bash
cd Nutrition_Recommendation_System
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv nutrition_venv
```

### Activate Virtual Environment

```bash
nutrition_venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run the Application

```bash
python app.py
```

---

## 6️⃣ Open Browser

```
http://127.0.0.1:5000
```

---

# 📦 Required Libraries

- Flask
- pandas
- numpy
- scikit-learn
- joblib

Install manually:

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

# 📈 Working Process

```text
User Input
      │
      ▼
Enter Nutrition Values
      │
      ▼
StandardScaler
      │
      ▼
K-Means Clustering
      │
      ▼
Predict Similar Cluster
      │
      ▼
Euclidean Distance
      │
      ▼
Top 10 Meal Recommendations
      │
      ▼
Display Results
```

---

# 🚀 Future Improvements

- 🔐 User Authentication
- 📅 Weekly Diet Planner
- 📊 Daily Calorie Tracker
- 🤖 AI Nutrition Chatbot
- 📄 PDF Diet Report
- 🗄 Database Integration
- ❤️ Health Goal Recommendation
- 📱 Mobile Responsive Dashboard
- ☁ Cloud Deployment
- 🧠 Deep Learning Recommendation System

---

# 👨‍💻 Author

## **Krishan Kumar Saini**

**Computer Science Engineering Student**

### Interests

- Machine Learning
- Data Science
- Artificial Intelligence
- Deep Learning
- Generative AI
- Web Development

### GitHub

https://github.com/KrishanSaini01

---

# ⭐ Support

If you like this project, please give it a **⭐ Star** on GitHub.

Your support motivates me to build more **Machine Learning, Artificial Intelligence, and Data Science Projects**.

---

# 📄 License

This project is developed for **educational and learning purposes**.

Feel free to use, modify, and improve it for academic and personal projects.