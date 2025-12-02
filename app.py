import json
from flask import Flask, render_template_string, request, redirect, url_for

# Initialize the Flask application
app = Flask(_name_)

# --- In-Memory Database (A list of task dictionaries) ---
# In a real application, this data would come from a database (like Firestore or SQLite).
# We initialize it with some sample data.
tasks = [
    {"id": 1, "title": "Finalize Project 6 Terraform Module", "completed": False},
    {"id": 2, "title": "Collaborate on Project 10 CI/CD integration", "completed": False},
    {"id": 3, "title": "Patch Kubernetes ImagePullSecrets issue", "completed": True},
]
next_id = 4 # Simple counter for new tasks

# --- HTML Template (Using Tailwind CSS for a neat look) ---
# This is an immersive HTML template placed directly in the Python file for simplicity.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Task Manager</title>
    <!-- Tailwind CSS CDN for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom scrollbar for better aesthetics */
        body { font-family: 'Inter', sans-serif; background-color: #f7f9fc; }
        .task-list { max-height: 60vh; overflow-y: auto; }
        .task-list::-webkit-scrollbar { width: 8px; }
        .task-list::-webkit-scrollbar-thumb { background-color: #cbd5e1; border-radius: 4px; }
        .task-list::-webkit-scrollbar-track { background-color: #f1f1f1; }
    </style>
</head>
<body class="p-8">

    <div class="max-w-4xl mx-auto bg-white p-6 md:p-10 rounded-xl shadow-2xl">
        <h1 class="text-4xl font-extrabold text-gray-800 mb-6 border-b-2 border-indigo-100 pb-3">
            DevOps Task Manager 📋
        </h1>
        <p class="text-gray-500 mb-8">
            Manage your infrastructure and application deployment tasks.
        </p>

        <!-- Task Addition Form -->
        <form method="POST" action="{{ url_for('add_task') }}" class="flex mb-8 space-x-3">
            <input type="text" name="title" placeholder="Add a new task (e.g., Set up AKS cluster)" required
                   class="flex-grow p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 transition duration-150">
            <button type="submit"
                    class="bg-indigo-600 text-white px-5 py-3 rounded-lg font-semibold hover:bg-indigo-700 transition duration-150 shadow-md">
                Add Task
            </button>
        </form>

        <!-- Task List Header -->
        <div class="flex justify-between items-center text-gray-600 font-bold border-b pb-2 mb-4">
            <span class="w-1/12">Done</span>
            <span class="w-9/12">Task Description</span>
            <span class="w-2/12 text-right">Actions</span>
        </div>

        <!-- Task List -->
        <div class="task-list space-y-3">
            {% for task in tasks %}
            <div class="flex items-center p-4 rounded-lg transition duration-200 
                {% if task.completed %} 
                    bg-green-50 text-gray-400 line-through 
                {% else %} 
                    bg-white hover:bg-gray-50 shadow-sm 
                {% endif %}">
                
                <!-- Status Checkbox -->
                <form method="POST" action="{{ url_for('toggle_task', task_id=task.id) }}" class="w-1/12">
                    <input type="checkbox" name="completed" onchange="this.form.submit()" 
                           {% if task.completed %} checked {% endif %}
                           class="h-5 w-5 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500 cursor-pointer">
                </form>

                <!-- Task Title -->
                <span class="w-9/12 text-gray-800">
                    {{ task.title }}
                </span>

                <!-- Delete Button -->
                <form method="POST" action="{{ url_for('delete_task', task_id=task.id) }}" class="w-2/12 text-right">
                    <button type="submit" 
                            class="text-red-500 hover:text-red-700 text-sm font-medium transition duration-150 p-2 rounded-full hover:bg-red-100">
                        Delete
                    </button>
                </form>
            </div>
            {% endfor %}
            
            {% if not tasks %}
            <div class="text-center py-8 text-gray-500 italic">No tasks yet! Add one above to get started.</div>
            {% endif %}
        </div>
    </div>
</body>
</html>
"""

# --- Flask Routes ---

@app.route('/')
def index():
    """Displays the main task list page."""
    # Sort incomplete tasks first, then completed ones
    sorted_tasks = sorted(tasks, key=lambda x: x['completed'])
    return render_template_string(HTML_TEMPLATE, tasks=sorted_tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Handles adding a new task to the list."""
    global next_id
    title = request.form.get('title')
    if title:
        new_task = {"id": next_id, "title": title, "completed": False}
        tasks.append(new_task)
        next_id += 1
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    """Toggles the completion status of a task."""
    for task in tasks:
        if task['id'] == task_id:
            # Checkbox automatically sends 'on' if checked, so we toggle the status
            task['completed'] = not task['completed'] 
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Deletes a task from the list."""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

# Run the app
if _name_ == '_main_':
    # Flask will start and serve the application on http://127.0.0.1:5000/
    app.run(debug=True)