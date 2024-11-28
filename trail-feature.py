from models import trail_feature_schema, trail_features_schema, Trail_Feature
from config import db
from flask import make_response, abort

#Reads all entries - Tested - Works as intended
def read_all():
    trail_feature_id = Trail_Feature.query.all()
    return trail_features_schema.dump(trail_feature_id)


#Create - Tested - Works as intended
def create(trail_feature):
    trail_feature_id = trail_feature.get("trail_feature_id")
    trail_id = trail_feature.get("trail_id")

    existing_trail_feature = Trail_Feature.query.filter(Trail_Feature.trail_feature_id == trail_feature_id, Trail_Feature.trail_id == trail_id).one_or_none()

    if existing_trail_feature is None:
        new_trail_feature = trail_feature_schema.load(trail_feature, session=db.session)
        db.session.add(new_trail_feature)
        db.session.commit()
        return trail_feature_schema.dump(new_trail_feature), 201
    else:
        abort(406, f'Trail feature with trail feature ID {trail_feature_id} and trail ID {trail_id} already exists')


#Retrieve - Tested - Does not work ---> Needs remaking as requests for both trail_id and trail_feature_id
def retrieve(trail_id):
    trail_id = Trail_Feature.query.filter(Trail_Feature.trail_id == trail_id).one_or_none()
    trail_feature_id = Trail_Feature.query.all(Trail_Feature.trail_id == trail_id).one_or_none()

    if trail_id is not None:
        return trail_feature_schema.dump(trail_id), trail_feature_schema.dump(trail_feature_id)
    else:
        abort(404, f'Feature with trail feature ID {trail_id} cannot be found')


#Delete
