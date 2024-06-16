# Django Templates and Rendering

## Basic Task

### Render a Simple Template

1. **Task:** Create a simple Django view that renders an HTML template displaying a static message.
2. **Steps:**
   - Create a view in your app's `views.py` file that renders an HTML template.
   - Create a template that displays a static message like "Welcome to my website!".
   - Map the view to a URL pattern in your app's `urls.py` file.

## Intermediate Task

### Use Template Variables and Context

1. **Task:** Create a view that passes dynamic data to a template and displays it.
2. **Steps:**
   - Create a view in your app's `views.py` file that passes a context dictionary with some dynamic data to a template.
   - Create a template that uses template variables to display the dynamic data.
   - Create a URL pattern to map this view.

## Advanced Task

### Template Inheritance and Static Files

1. **Task:** Create a base template and extend it in other templates. Include static files (CSS/JS) in the templates.
2. **Steps:**
   - Create a base template with common HTML structure and static file links.
   - Create child templates that extend the base template and provide specific content.
   - Set up Django to serve static files and include some CSS/JS files in the templates.
   - Create views and URL patterns to render these templates.
