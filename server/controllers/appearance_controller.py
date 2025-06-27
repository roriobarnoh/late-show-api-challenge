from flask import Blueprint, request, jsonify
from app import db
from flask_jwt_extended import jwt_required
from models.appearance import Appearance

appearance_bp = Blueprint('appearance', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    if not 1 <= data["rating"] <= 5:
        return jsonify({"error": "Rating must be between 1 and 5"}), 400
    appearance = Appearance(
        guest_id=data["guest_id"],
        episode_id=data["episode_id"],
        rating=data["rating"]
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify({"message": "Appearance created"}), 201
