# Book-Recommendation-System
# 📚 Book Recommendation System

A web-based **Book Recommendation System** built using **Machine Learning, Flask, and Python** that suggests similar books based on user preferences using collaborative filtering.

---

## 🚀 Features

- Recommend books based on similarity scores
- Displays book title, author, rating, number of reviews, and cover image
- Handles missing or broken book cover images gracefully
- Clean and responsive UI
- Real-world data cleaning and preprocessing

---

## 🧠 How It Works

- Uses **collaborative filtering**
- Computes similarity between books using a precomputed similarity matrix
- When a user selects a book, the system recommends the top similar books
- Recommendations are based on user rating patterns

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **NumPy**
- **Pandas**
- **HTML / Tailwind CSS**
- **Pickle** (for serialized models and data)

---

## 📂 Project Structure


├── app.py
├── popular.pkl
├── pt.pkl
├── books.pkl
├── ratings.pkl
├── similarity_scores.pkl
├── templates/
│ ├── index.html
│ └── recommend.html
├── static/
└── README.md

---

## 🧹 Data Cleaning Highlights

- Filled missing image URLs with a placeholder image
- Converted all image URLs to secure HTTPS
- Handled duplicate book entries
- Ensured robust rendering even when data is incomplete

---

## ▶️ How to Run

1. Clone the repository
2. Install dependencies  
   ```bash
   pip install flask numpy


Run the app

python app.py


Open browser at

http://127.0.0.1:5000