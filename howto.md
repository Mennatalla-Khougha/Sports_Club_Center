To allow the admin to perform console functionality from the website, you need to create web interfaces (routes and views) for each of the console commands. Here's a general approach:

1. **Create new routes in your Flask application for each console command.** Each route should correspond to a specific console command. For example, you might have a route like `/admin/create` for the `create` command, `/admin/update` for the `update` command, and so on.

2. **Create forms for each route.** These forms will collect the necessary information from the admin to execute the corresponding command. For example, the form for the `create` command might ask for the class name and attributes.

3. **Handle form submissions in your route functions.** When the admin submits a form, the corresponding route function should take the form data, use it to execute the corresponding console command, and then return a response to the admin. This might involve calling functions from your `console.py` script, or it might involve duplicating some of the logic from that script in your route functions.

4. **Create views for each route.** These views will display the forms to the admin and show the results of the commands. You can use Flask's template engine to create these views.

Here's a simple example of what the route for the `create` command might look like:

```python
from flask import request, render_template
from console import ConsoleCommand

@app.route('/admin/create', methods=['POST', 'GET'])
def admin_create():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('admin_create.html', message="Instance created successfully")
    return render_template('admin_create.html')
```

In this example, `admin_create.html` is a template that displays a form for the admin to enter the class name and attributes. After the form is submitted, the `admin_create` function executes the `create` command with the form data and then re-renders the template with a success message.

You would need to create similar routes, forms, and views for all the other console commands. Note that this is a simplified example and you might need to add more error checking and other features in a real application.