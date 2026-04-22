#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    "title": [
        "Inception", "Interstellar", "The Dark Knight",
        "Avengers: Endgame", "Titanic", "The Notebook",
        "John Wick", "The Matrix", "Gladiator", "Toy Story"
    ],
    "genre": [
        "Sci-Fi Thriller", "Sci-Fi Drama", "Action Crime",
        "Action Superhero", "Romance Drama", "Romance",
        "Action Thriller", "Sci-Fi Action", "Action Drama", "Animation Family"
    ]
}

df = pd.DataFrame(data)

# Convert genres into vectors
cv = CountVectorizer()
matrix = cv.fit_transform(df["genre"])

# Compute similarity
similarity = cosine_similarity(matrix)

# Recommendation function
def recommend(movie_name):
    if movie_name not in df['title'].values:
        print("Movie not found!")
        return
    
    idx = df[df['title'] == movie_name].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print(f"\nMovies similar to '{movie_name}':\n")
    
    for i in sorted_scores[1:6]:
        print(df.iloc[i[0]]['title'])

# Test
recommend("Inception")


# In[ ]:




