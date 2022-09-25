from flask import Blueprint, render_template, request, jsonify
from .models import Ticket
from . import db

main = Blueprint('main', __name__)

@main.route("/ticket/list")
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([ticket.to_json() for ticket in tickets])

@main.route("/ticket", methods=["POST"])
def create_ticket():
    if not request.json:
        abort(400)
    new_ticket = Ticket(
                name=request.json.get("name"),
                phone=request.json.get("phone"),
                material=request.json.get("material"),
                email=request.json.get("email"),
                location=request.json.get("location"),
                model=request.json.get("model"),
                img=request.json.get("img")
            )
    db.session.add(new_ticket)
    db.session.commit()

    return jsonify(new_ticket.to_json()), 201

@main.route("/ticket/<int:id>", methods=["PUT"])
def update_ticket(idd):
    if not request.json:
        abort(400)

    ticket = Ticket.query.get(idd)
    if ticket is None:
        abort(404)

    ticket.name = request.json.get("name", ticket.name)
    ticket.phone = request.json.get("phone", ticket.phone)
    ticket.material = request.json.get("material", ticket.material)
    ticket.email = request.json.get("email", ticket.email)
    ticket.location = request.json.get("location", ticket.location)
    ticket.model = request.json.get("model", ticket.model)
    ticket.img = request.json.get("img", ticket.img)
    
    db.session.commit()
    
    return jsonify(ticket.to_json())


