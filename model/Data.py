import pymongo
import json
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.logger import Info_Log, Warning_Log


# Load Article data from JSON file
article = os.path.join(os.path.dirname(__file__), 'Data_Article.json')
author = os.path.join(os.path.dirname(__file__), 'Data_Author.json')

with open(article) as f:
    article_data = json.load(f)

# Load Author data from JSON file
with open(author) as f:
    author_data = json.load(f)

# Connect to MongoDB
client = pymongo.MongoClient('mongodb+srv://bhhoang:Ilove1000@nanikaclustor.mlolje2.mongodb.net/?retryWrites=true&w=majority')
db = client['newspapers_db']
Info_Log("Connected to the database successfully.")
Info_Log("Inserting data...")
# Drop all collections in the database
db.drop_collection('newspapers')
db.drop_collection('authors')
Warning_Log("Old database dropped.")

# Insert Article data into MongoDB
collection = db['newspapers']
collection.insert_many(article_data['Articles'])
Info_Log("Article data inserted.")

# Insert Author data into MongoDB
collection = db['authors']
collection.insert_many(author_data['Authors'])
Info_Log("Author data inserted.")

# Update publication history of authors
for article in article_data['Articles']:
    author_id = article['author']
    article_id = article['_id']
    collection.update_one(
        {'_id': author_id},
        {'$push': {'publication': article_id}}
    )
Info_Log("Publication history updated.")
Info_Log("Data inserted successfully.")