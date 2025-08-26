import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset and create embeddings (global for testing)
df = pd.read_csv('movies.csv')
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(df['plot'].tolist(), convert_to_tensor=False)

def search_movies(query, top_n=5):
    """
    Performs a semantic search for movies based on a query.
    """
    # Encode the query to a vector
    query_embedding = model.encode(query, convert_to_tensor=False)
    
    # Calculate cosine similarity between the query and all movie plots
    similarities = cosine_similarity([query_embedding], embeddings)[0]
    
    # Get the indices of the top_n most similar movies
    top_n_indices = similarities.argsort()[-top_n:][::-1]
    
    # Create a DataFrame with the top results
    results = df.iloc[top_n_indices].copy()
    results['similarity'] = similarities[top_n_indices]
    
    return results[['title', 'plot', 'similarity']]

if __name__ == '__main__':
    # Example usage:
    query = "Action-adventure film about two small-time crooks"
    top_results = search_movies(query, top_n=3)
    print(top_results)