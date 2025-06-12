from flask import Blueprint, request, jsonify
from app.models import Learners
from app import db

create_bp = Blueprint('create', __name__, url_prefix='/learners')

@create_bp.route('/', methods=['POST'])
def create_learner():
    data = request.get_json()
    learner = Learners(
        national_id=data.get('national_id'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        course_name=data.get('course_name'),
        email=data.get('email'),
        phone=data.get('phone'),
        county=data.get('county')
    )
    db.session.add(learner)
    db.session.commit()
    return jsonify({"message": "Learner created", "id": learner.school_id}), 201
