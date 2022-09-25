from . import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    phone = db.Column(db.Integer)
    material = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    location = db.Column(db.String(1000))
    model = db.Column(db.String(1000))
    img = db.Column(db.String(1000))

    def to_json(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "material": self.material,
            "email": self.email,
            "location": self.location,
            "model": self.model,
            "img": self.img
        }
