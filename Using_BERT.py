import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

# def preprocess_data(data):
#     # Perform any required preprocessing on the data
#     # For example, cleaning, lowercasing, etc.
#     pass

def encode_descriptions(data, model):
    descriptions = [item['description'] for item in data]
    encoded_descriptions = model.encode(descriptions)
    for i, item in enumerate(data):
        item['vector'] = encoded_descriptions[i]
    return data

def calculate_similarity(query, model, data):
    query_vector = model.encode([query])[0]
    similarity_scores = cosine_similarity([query_vector], [item['vector'] for item in data])[0]
    return similarity_scores

def get_top_similar_items(similarity_scores, data, top_n):
    top_indices = similarity_scores.argsort()[::-1][:top_n]
    top_items = [data[i] for i in top_indices]
    return top_items

# Specify the file path of the JSON data
data_file = 'product_info.json'

# Load the JSON data
data = load_data(data_file)

# # Preprocess the data
# preprocess_data(data)

# Load the BERT model
model = SentenceTransformer('bert-base-nli-mean-tokens')

# Encode the descriptions using the BERT model
data = encode_descriptions(data, model)

# Preprocess the query
query = 'white shirt'

# Calculate similarity scores between the query and dataset descriptions
similarity_scores = calculate_similarity(query, model, data)

# Specify the number of top similar items to retrieve
top_n = 10

# Get the top-N most similar items based on the similarity scores
top_similar_items = get_top_similar_items(similarity_scores, data, top_n)

# Return the top similar item links as output
similar_item_links = [item['link'] for item in top_similar_items]
print(similar_item_links)
