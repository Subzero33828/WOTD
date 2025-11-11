
from flask import Flask, request, jsonify

from models import db, Note

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# ------------------------
# ROUTES
# ------------------------

@app.route("/")
def hello():
    return "Hello, Flask!"

# Get all notes
@app.route("/notes", methods=['GET'])
def get_notes():
    notes = Note.query.all()  # Retrieve all notes
    return jsonify([note.to_dict() for note in notes])

# Add a new note
@app.route("/notes", methods=['POST'])
def add_note():
    data = request.get_json()  # Get JSON from request
    # Validate input
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    # Create and save new note
    new_note = Note(title=data['title'], content=data['content'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.to_dict()), 201

# Search notes by keyword
@app.route("/notes/search", methods=['GET'])
def search_notes():
    query = request.args.get('query', '')  # Get query parameter
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Filter notes where title or content contains the query (case-insensitive)
    results = Note.query.filter(
        (Note.title.ilike(f"%{query}%")) | (Note.content.ilike(f"%{query}%"))
    ).all()

    return jsonify([note.to_dict() for note in results])
