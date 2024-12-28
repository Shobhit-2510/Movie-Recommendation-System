import pickle
import pandas as pd
import difflib as dl
import streamlit as st

# importing movies data
movies_data = pd.read_csv("movies.csv")

# Load the saved similarity matrix
with open('similarity.pkl', 'rb') as f:
    loaded_similarity = pickle.load(f)
    
def movie_recommendation(movie_name):
    
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = dl.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(loaded_similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

    return sorted_similar_movies

def main():
    st.title('Movie Recommendation System')
    
    movie_name = st.text_input('Enter the movie name')
    
    if st.button('Recommend'):
        sorted_similar_movies = movie_recommendation(movie_name)
        i = 1
        for movie in sorted_similar_movies:
            index = movie[0]
            title_from_index = movies_data[movies_data.index==index]['title'].values[0]
            if (i<31):
                st.write(f'{i}. {title_from_index}')
                i += 1
                
if __name__ == '__main__':
    main()