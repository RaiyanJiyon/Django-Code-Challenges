# Django Models and Data Handling

## Basic Task

### Create a Simple Model and Save Data

1. **Task:** Create a simple Django model to represent a Book with fields for the title and author. Save a few instances of this model to the database.
2. **Steps:**
   - Define a Book model in your app's `models.py` file with fields for title and author.
   - Make and apply migrations to create the corresponding database table.
   - Use the Django shell or an admin interface to create and save a few Book instances.

## Intermediate Task

### Query and Display Data from a Model

1. **Task:** Create a view that queries all Book instances from the database and displays them in a template.
2. **Steps:**
   - Define a view in your app's `views.py` file that queries all Book objects using Django's ORM.
   - Pass the list of Book objects to a template.
   - Create a template to loop through the Book objects and display their details.
   - Create a URL pattern to map this view.

## Advanced Task

### Model Relationships and Advanced Queries

1. **Task:** Create a Publisher model and establish a relationship with the Book model. Implement a view that displays books published by a specific publisher.
2. **Steps:**
   - Define a Publisher model in your app's `models.py` file.
   - Modify the Book model to include a ForeignKey relationship to the Publisher model.
   - Make and apply migrations to update the database schema.
   - Create a view that accepts a `publisher_id` parameter, queries for all books by that publisher, and passes the results to a template.
   - Create a URL pattern to map this view, capturing the `publisher_id` from the URL.
