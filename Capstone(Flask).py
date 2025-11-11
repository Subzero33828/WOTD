# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     done = db.Column(db.Boolean, default=False)

# with app.app_context():
#     db.create_all()

# @app.route("/tasks", methods=["GET"])
# def get_tasks():
#     tasks = Task.query.all()
#     return jsonify([{"id": task.id, "title": task.title, "done": task.done} for task in tasks])

# @app.route("/tasks", methods=["POST"])
# def add_task():
#     data = request.get_json()
#     new_task = Task(title=data['title'])
#     db.session.add(new_task)
#     db.session.commit()
#     return jsonify({"message": "Task added"}), 201

# @app.route("/tasks/<int:task_id>", methods=["PUT"])
# def update_task(id):
#     task = Task.query.get_or_404(id)
#     data = request.get_json()
#     task.title = data.get('title', task.title)
#     task.done = data.get('done', task.done)
#     db.session.commit()
#     return jsonify({"message": "Task updated"})

# @app.route("/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(id):
#     task = Task.query.get_or_404(id)
#     db.session.delete(task)
#     db.session.commit()
#     return jsonify({"message": "Task deleted"})

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ----------------------
# Database Model
# ----------------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Create tables
with app.app_context():
    db.create_all()

# ----------------------
# Helper Functions
# ----------------------
def validate_task_data(data):
    if not data or "title" not in data or not data["title"].strip():
        return False
    return True

# ----------------------
# Routes
# ----------------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Pagination parameters
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    tasks_query = Task.query.paginate(page=page, per_page=per_page, error_out=False)
    tasks = [
        {"id": task.id, "title": task.title, "done": task.done}
        for task in tasks_query.items
    ]

    return jsonify({
        "tasks": tasks,
        "total": tasks_query.total,
        "page": tasks_query.page,
        "pages": tasks_query.pages
    })

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not validate_task_data(data):
        return jsonify({"error": "Invalid input. 'title' is required."}), 400

    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added", "id": new_task.id}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input provided."}), 400

    title = data.get('title', task.title)
    done = data.get('done', task.done)
    if title.strip() == "":
        return jsonify({"error": "Title cannot be empty."}), 400

    task.title = title
    task.done = done
    db.session.commit()
    return jsonify({"message": "Task updated"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

@app.route("/tasks/search", methods=["GET"])
def search_tasks():
    keyword = request.args.get("keyword", "")
    if not keyword.strip():
        return jsonify({"error": "Keyword cannot be empty."}), 400

    results = Task.query.filter(Task.title.contains(keyword)).all()
    return jsonify([
        {"id": task.id, "title": task.title, "done": task.done}
        for task in results
    ])

# ----------------------
# Run Server
# ----------------------
if __name__ == "__main__":
    app.run(debug=True)
  