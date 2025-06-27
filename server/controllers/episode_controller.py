from flask import Blueprint, jsonify, request
from models.episode import Episode
from app import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{"guest_id": a.guest_id, "rating": a.rating} for a in episode.appearances]
    return jsonify({"id": episode.id, "date": episode.date, "number": episode.number, "appearances": appearances})

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": "Episode deleted"}), 200
