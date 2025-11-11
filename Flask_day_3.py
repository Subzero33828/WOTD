from flask import Flask, request, jsonify
# =========================

app = Flask(__name__)

notes = []

@app.route('/')
def hello():
    return "Hello, Flask!"

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json() #expect {"content": "some txt"}

    # Validate that data exists and has a 'note' key
    if not data or 'content' not in data:
        return jsonify({"error": "Invalid data"}), 400
    

    note = {"id": len(notes) + 1, "content": data["content"]}
    
    # Append the new note to the notes list
    notes.append(note)
    return jsonify(note), 201

if __name__ == "__main__":
    app.run(debug=True)