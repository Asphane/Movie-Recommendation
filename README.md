# <div align="center">

## 🎬✨ <span style="font-size:40px; font-weight:700;">Movie Recommendation System</span>

A Modern Content-Based Recommender App Built with **Streamlit + TMDB API**

</div>

---

<p align="center">
  <img src="https://img.shields.io/github/repo-size/Asphane/Movie-Recommendation?color=blue&style=for-the-badge">
  <img src="https://img.shields.io/github/languages/top/Asphane/Movie-Recommendation?color=brightgreen&style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python">
</p>

---

## 🚀 **Overview**

This **Movie Recommendation System** uses **content-based filtering** to recommend similar movies based on metadata and cosine similarity.
It integrates with the **TMDB API** to fetch **high-quality posters**, providing a clean and modern UI built using Streamlit.

The project is lightweight, fast, and ready for deployment.

---

## 🌟 **Key Features**

✨ **Content-based filtering** using cosine similarity
🎞️ **Real-time posters** fetched via TMDB API
⚡ **Optimized response time** using Session-based requests
🎨 **Sleek Streamlit UI** with responsive layout
📦 **Pickle-based model loading** (lightweight & quick)
🔍 **Accurate recommendations** from metadata vectors

---

## 🧰 **Tech Stack**

| Component            | Technology                |
| -------------------- | ------------------------- |
| **Frontend/UI**      | Streamlit                 |
| **Backend Logic**    | Python                    |
| **Data Handling**    | Pandas, Pickle            |
| **API**              | TMDB (The Movie Database) |
| **Similarity Model** | Cosine Similarity         |

---

# 📂 **Project Structure**

```bash
Movie-Recommendation/
│── app.py
│── movie_list.pkl
│── similarity.pkl
│── requirements.txt
│── README.md
```

---

# ⚙️ **Installation & Setup**

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/Asphane/Movie-Recommendation.git
cd Movie-Recommendation
```

### **2️⃣ Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### **3️⃣ Install required dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Add TMDB API Token**

Inside `app.py`, replace:

```python
"Authorization": "Bearer YOUR_TOKEN_HERE"
```

with your actual **TMDB Read Access Token (v4)**.

---

# ▶️ **Run the Application**

```bash
streamlit run app.py
```

App runs at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

# 🧠 **How It Works**

### 🔹 Step 1 — Load Metadata

Reads `movie_list.pkl` which contains movie vectors & metadata.

### 🔹 Step 2 — Load Similarity Matrix

Loads pre-computed cosine similarity from `similarity.pkl`.

### 🔹 Step 3 — Recommend Movies

Finds top N most similar movies based on the selected movie.

### 🔹 Step 4 — Fetch Posters

Uses TMDB API to fetch high-resolution posters.

### 🔹 Step 5 — Display in Streamlit

Renders posters and titles in a clean grid layout.

---

# 🌄 **Screenshots**

> *(Add your screenshot images here)*
> Example:

```html
<p align="center">
  <img src="assets/app_preview.png" width="80%">
</p>
```

---

# 🔧 **Troubleshooting**

### ❗ *Poster not loading*

* Invalid or expired TMDB token
* Missing "Bearer " prefix
* API rate limit possibly hit

### ❗ *Git not detecting repo*

```bash
git init
git remote add origin https://github.com/Asphane/Movie-Recommendation.git
```

---

# 🤝 **Contributing**

Contributions are welcome!
You can help improve:

* UI Design
* Advanced recommendation algorithms
* Model training
* Deployments (Streamlit Cloud / Render / HuggingFace Spaces)

Feel free to submit a **pull request**.

---

# 📜 **License**

Licensed under the **MIT License**.

---

# ⭐ **Support the Project**

If this project helped you, please ⭐ the repo!
It motivates me to build more cool ML apps.

---
