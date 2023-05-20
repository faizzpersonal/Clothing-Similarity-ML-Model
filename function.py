import json
import tensorflow_hub as hub
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def preprocess_data(data):
    # Perform any required preprocessing on the data
    # For example, cleaning, lowercasing, etc.
    pass

def encode_descriptions(descriptions, encoder):
    embeddings = encoder(descriptions)
    return embeddings.numpy()

def calculate_similarity(query_embedding, data_embeddings):
    similarity_scores = cosine_similarity([query_embedding], data_embeddings)[0]
    return similarity_scores

def get_top_similar_items(similarity_scores, data, top_n):
    top_indices = similarity_scores.argsort()[::-1][:top_n]
    top_items = [data[i] for i in top_indices]
    return top_items

# Specify the file path of the JSON data
data_file = 'product_info.json'

# Load the JSON data
data = load_data(data_file)

# Preprocess the data
preprocess_data(data)

# Load the Universal Sentence Encoder model
encoder = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")

# Extract the descriptions from the data
descriptions = [item['description'] for item in data]

# Preprocess the query
query = 'brown shirt'

# Preprocess the query and dataset descriptions
all_descriptions = [query] + descriptions
all_embeddings = encode_descriptions(all_descriptions, encoder)

# Separate the query embedding from the dataset embeddings
query_embedding = all_embeddings[0]
data_embeddings = all_embeddings[1:]

# Calculate similarity scores between the query and dataset descriptions
similarity_scores = calculate_similarity(query_embedding, data_embeddings)

# Specify the number of top similar items to retrieve
top_n = 5

# Get the top-N most similar items based on the similarity scores
top_similar_items = get_top_similar_items(similarity_scores, data, top_n)

# Return the top similar item links as output
similar_item_links = [item['link'] for item in top_similar_items]
print(similar_item_links)
