#thisischatcode
@app.route("/notes", methods=["POST"])
def add_note():
    # Get JSON data from the request; expecting something like {"content": "some text"}
    data = request.get_json()

    # Validate that data exists and contains the "content" key
    if not data or 'content' not in data:
        # If input is missing or invalid, return an error with status code 400
        return jsonify({"error": "Invalid data"}), 400

    # Create a new note with a unique ID and the content from the request
    note = {
        "id": len(notes) + 1,  # simple incremental ID based on current list length
        "content": data["content"]
    }

    # Append the new note to the notes list
    notes.append(note)

    # Return the newly created note with status code 201 (created)
    return jsonify(note), 201

    # ---------------------------------------------------------
    # Developer Note: How to test this route using PowerShell curl
    # GET all notes:
    #   curl http://127.0.0.1:5000/notes
    #
    # POST a new note:
    #   curl -Method POST http://127.0.0.1:5000/notes `
    #        -Body '{"content":"My first note"}' `
    #        -ContentType "application/json"
    #
    # After POST, GET again to see the new note in the notes array.
    # ---------------------------------------------------------

# Input validation → ensures the user sent a proper note.

# id: len(notes)+1 → gives each note a unique ID.

# notes.append(note) → stores the note in memory.

# return jsonify(note), 201 → confirms the note was added.