import csv
from pymongo import MongoClient

class Newspaper:
    def __init__(self, country, city, date, categories, viewed, title, description, content, author, id_News):
        self.id_News = id_News
        self.country = country
        self.city = city
        self.date = date
        self.categories = categories
        self.viewed = viewed
        self.title = title
        self.description = description
        self.content = content
        self.author = author

class Author:
    def __init__(self, name, dob, email, bio, expertise, publication_history, id_Author):
        self.id_Author = id_Author
        self.name = name
        self.dob = dob
        self.email = email
        self.bio = bio
        self.expertise = expertise
        self.publication_history = publication_history

# Open the CSV file
with open('News_Dataset.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Connect to the MongoDB database
    client = MongoClient('mongodb://localhost:27017/')
    db = client['newspapers_db']
    newspapers_collection = db['newspapers']
    authors_collection = db['authors']

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Create a dictionary for the current row
        newspapers_data = {
            '_id': row['ID_News'],
            'country': row['Country'],
            'city': row['City'],
            'date': row['Date'],
            'categories': row['Categories'],
            'viewed': row['Viewed'],
            'title': row['Title'],
            'description': row['Description'],
            'content': row['Content'],
            'author': row['Author']
        }

        authors_data = {
            '_id': row['ID_Author'],
            'name': row['Name'],
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
            print(f"Newspaper with title: {existing_newspapers['title']} already exists in the database.")
            existing_authors = authors_collection.find_one({
                '_id': row['ID_Author'],
                'name': row['Name']
            })
            if existing_authors:
                print(f"Author with ID: {existing_authors['_id']} and {existing_authors['name']} already exists in the database.")
            else:
                # Insert the author data
                authors_collection.insert_one(authors_data)
        else:
            # Insert the newspaper data
            newspapers_collection.insert_one(newspapers_data)

            # Insert the author data
            authors_collection.insert_one(authors_data)
            
    print("Done inserting data.")