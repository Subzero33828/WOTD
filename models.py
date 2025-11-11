from flask_sqlalchemy import SQLAlchemy

# Initialize the ORM
db = SQLAlchemy()

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique, auto-incremented ID
    title = db.Column(db.String(100), nullable=False)  # Note title, required
    content = db.Column(db.Text, nullable=False)       # Note content, required

    def to_dict(self):
        """
        Convert Note object to dictionary for JSON responses.
        """
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }
  
    