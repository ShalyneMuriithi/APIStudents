from flask import Blueprint, request, jsonify
from app.models import Learners
from app import db

update_bp = Blueprint('update', __name__, url_prefix='/learners')

@update_bp.route('/<int:id>', methods=['PUT'])
def update_learner(id):
    learner = Learners.query.get_or_404(id)
    data = request.get_json()

    learner.national_id = data.get('national_id', learner.national_id)
    learner.first_name = data.get('first_name', learner.first_name)
    learner.last_name = data.get('last_name', learner.last_name)
    learner.course_name = data.get('course_name', learner.course_name)
    learner.email = data.get('email', learner.email)
    learner.phone = data.get('phone', learner.phone)
    learner.county = data.get('county', learner.county)

    db.session.commit()
    return jsonify({"message": "Learner updated", "id": learner.school_id}), 200
