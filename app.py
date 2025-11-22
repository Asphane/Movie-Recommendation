# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# def fetch_poster(movie_id):
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNTFmZGJmMGRjNTgwN2E2Y2Q1Yjc2NmE5MDA5OGQxYSIsIm5iZiI6MTc2Mzc4MTMzMy45Niwic3ViIjoiNjkyMTJhZDUyZWNhMWRiZGQ1ZGNmM2FiIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.P-kwDEAVYuZ--Luhm6h-JyNP8BABeEzrCwteTD_d3HQ",
#         "accept": "application/json"
#     }

#     url = f"https://api.themoviedb.org/3/movie/{movie_id}"
#     data = requests.get(url, headers=headers).json()

#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



# movie_option = pickle.load(open('movie_list_dict.pkl', 'rb'))
# movies = pd.DataFrame(movie_option)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# def recommend(movie_name):
#     idx = movies[movies['title'] == movie_name].index[0]
#     distance = similarity[idx]
#     movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

#     recommended_movies = []
#     recommended_movies_poster = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id

#         recommended_movies_poster.append(fetch_poster(movie_id))
#         recommended_movies.append(movies.iloc[i[0]].title)

#     return recommended_movies, recommended_movies_poster

# st.title("Movie Recommendation System")

# selected_movie = st.selectbox(
#     "How would you like to be contacted?",
#     movies['title'].values
# )

# st.write("You selected:", selected_movie)

# if st.button('recommend'):
#     recommended_movie_name, recommended_movie_poster = recommend(selected_movie)

#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(recommended_movie_name[0])
#         st.image(recommended_movie_poster[0])
#     with col2:
#         st.text(recommended_movie_name[1])
#         st.image(recommended_movie_poster[1])

#     with col3:
#         st.text(recommended_movie_name[2])
#         st.image(recommended_movie_poster[2])
#     with col4:
#         st.text(recommended_movie_name[3])
#         st.image(recommended_movie_poster[3])
#     with col5:
#         st.text(recommended_movie_name[4])
#         st.image(recommended_movie_poster[4])


import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# -----------------------------
# FIX: Force HTTP/1.1 + Retries
# -----------------------------
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    backoff_factor=1
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)


# -----------------------------
# TMDB Poster Fetch Function
# -----------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNTFmZGJmMGRjNTgwN2E2Y2Q1Yjc2NmE5MDA5OGQxYSIsIm5iZiI6MTc2Mzc4MTMzMy45Niwic3ViIjoiNjkyMTJhZDUyZWNhMWRiZGQ1ZGNmM2FiIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.P-kwDEAVYuZ--Luhm6h-JyNP8BABeEzrCwteTD_d3HQ",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = session.get(url, headers=headers, timeout=10)
    data = response.json()

    poster_path = data.get("poster_path")

    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"


# -----------------------------
# Load Data
# -----------------------------
movie_option = pickle.load(open('movie_list_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_option)
similarity = pickle.load(open('similarity.pkl', 'rb'))

print(movies.columns)
print(movies.head())


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie_name):
    idx = movies[movies['title'] == movie_name].index[0]
    distance = similarity[idx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']   # Correct column
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button('Recommend'):
    recommended_movie_name, recommended_movie_poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_name[0])
        st.image(recommended_movie_poster[0])

    with col2:
        st.text(recommended_movie_name[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.text(recommended_movie_name[2])
        st.image(recommended_movie_poster[2])

    with col4:
        st.text(recommended_movie_name[3])
        st.image(recommended_movie_poster[3])

    with col5:
        st.text(recommended_movie_name[4])
        st.image(recommended_movie_poster[4])
