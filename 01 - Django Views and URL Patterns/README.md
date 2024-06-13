# Django Views and URL Patterns

## Basic Task

### Create a Basic View and URL Pattern

1. **Task:** Create a basic Django view that returns a simple "Hello, World!" response.
2. **Steps:**
   - Set up a new Django project and app if you haven't already.
   - Create a view in your app's `views.py` file that returns an HTTP response with the text "Hello, World!".
   - Map this view to a URL pattern in your app's `urls.py` file, so that visiting `http://yourserver/hello/` displays the "Hello, World!" message.

## Intermediate Task

### Dynamic URL Pattern and View with Template

1. **Task:** Create a view that accepts a username from the URL and displays a personalized greeting using a Django template.
2. **Steps:**
   - Create a view in your app's `views.py` file that captures a username parameter from the URL.
   - Pass the username to a template and render a personalized greeting message, such as "Hello, [username]!".
   - Create the corresponding URL pattern in your app's `urls.py` file to capture the username from the URL.

## Advanced Task

### Class-Based Views and URL Patterns with Parameters

1. **Task:** Create a class-based view (CBV) that handles HTTP GET and POST requests. The view should display a form on GET and process the form data on POST, then display the submitted data back to the user.
2. **Steps:**
   - Create a class-based view that inherits from Django's `View` class.
   - Implement the `get` method to display a form where the user can enter their name.
   - Implement the `post` method to process the form data, validate it, and then display a message with the submitted name.
   - Create a form class in Django to handle the form structure and validation.
   - Update the URL pattern in your app's `urls.py` file to use this class-based view.
