from flask import Blueprint, jsonify
from app.models import Learners

read_bp = Blueprint('read', __name__, url_prefix='/learners')

@read_bp.route('/', methods=['GET'])
def get_learners():
    learners = Learners.query.all()
    return jsonify([
    {
        "id": l.school_id,
        "name": f"{l.first_name} {l.last_name}",
        "email": l.email,
        "national_id": l.national_id,
        "course_name": l.course_name,
         "phone": l.phone
} for l in learners])

@read_bp.route('/<int:id>', methods=['GET'])
def get_learner(id):
    learner = Learners.query.get_or_404(id)
    return jsonify({
    "id": learner.school_id,
    "name": f"{learner.first_name} {learner.last_name}",
    "email": learner.email,
    "national_id": learner.national_id,
    "course_name": learner.course_name,
    "phone": learner.phone
    })




