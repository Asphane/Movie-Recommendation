import streamlit as st
import pickle
import pandas as pd
import requests



movie_option = pickle.load(open('movie_list_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_option)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):
    idx = movies[movies['title'] == movie_name].index[0]
    distance = similarity[idx]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies_poster.append(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_movies_poster

st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)

st.write("You selected:", selected_movie)

if st.button('recommend'):
    recommended_movie_name, recommended_movie_poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.beta_columns(5)
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
