import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv
from pymongo import MongoClient
from utils.logger import Info_Log, Warning_Log
from model.methods import limit_word

# Path to the CSV file
path = os.path.join(os.path.dirname(__file__), 'News_Dataset.csv')

# Open the CSV file
with open(path) as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Connect to the MongoDB database
    client = MongoClient('mongodb+srv://bhhoang:Ilove1000@nanikaclustor.mlolje2.mongodb.net/?retryWrites=true&w=majority')
    if ('--nukedb' in sys.argv):
        client.drop_database('newspapers_db')
        client.drop_database('authors_db')
        Warning_Log("Old database dropped.")
    db = client['newspapers_db']
    newspapers_collection = db['newspapers']
    authors_collection = db['authors']
    #print("[ INFO ] Connected to the database successfully.")
    #print("[ INFO ] Inserting data...")
    Info_Log("Connected to the database successfully.")
    Info_Log("Inserting data...")
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Create a dictionary for the current row
        newspapers_data = {
            '_id': row['ID_New'],
            'country': row['Country'],
            'city': row['City'],
            'date': row['Date'],
            'categories': row['Categories'],
            'viewed': row['Viewed'],
            'title': row['Title'],
            'description': limit_word(row['Description'], 50),
            'content': row['Content'],
            'author': row['Author']
        }

        authors_data = {
            '_id': row['ID_Author'],
            'name': row['Author_Name'],
            'dob': row['DoB'],
            'email': row['Email'],
            'bio': row['Bio'],
            'expertise': row['Expertise'],
            'publication_history': row['Publication History']
        }
        
        # Check if the newspaper already exists in the database
        existing_newspapers = newspapers_collection.find_one({
            'title': row['Title'],
            'description': row['Description']
        })
        
        if existing_newspapers:
            Warning_Log(f"Newspaper with title: {existing_newspapers['title']} already exists in the database.")
            existing_authors = authors_collection.find_one({
                '_id': row['ID_Author'],
                'name': row['Author_Name']
            })
            if existing_authors:
                Warning_Log(f"Author with ID: {existing_authors['_id']} and {existing_authors['name']} already exists in the database.")
            else:
                # Insert the author data
                authors_collection.insert_one(authors_data)
        else:
            # Insert the newspaper data
            newspapers_collection.insert_one(newspapers_data)

            # Insert the author data
            authors_collection.insert_one(authors_data)
            
    Info_Log("Finished seeding the database with sample data.")