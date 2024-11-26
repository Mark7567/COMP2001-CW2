from models import feature_schema, features_schema, Feature
from config import db
from flask import make_response, abort

def read_all():
    feature = Feature.query.all()
    return features_schema.dump(feature)


#Create
def create(feature):
    trail_feature_id = feature.get("trail_id")
    existing_feature = Feature.query.filter(Feature.trail_feature_id == trail_feature_id).one_or_none()

    if existing_feature is None:
        new_feature = feature_schema.load(feature, session=db.session)
        db.session.add(new_feature)
        db.session.commit()
        return feature_schema.dump(new_feature), 201
    else:
        abort(406, f'Feature with trail feature ID {trail_feature_id} already exists')


#Retrieve
def retrieve(trail_feature_id):
    feature = Feature.query.filter(Feature.trail_feature_id == trail_feature_id).one_or_more()

    if feature is not None:
        return feature_schema.dump(feature)
    else:
        abort(404, f'Feature with trail feature ID {trail_feature_id} cannot be found')


#Update Trail Feature
def updateTrailFeature(trail_feature_id, feature):
    existing_feature = Feature.query.filter(Feature.trail_feature_id == trail_feature_id).one_or_none()

    if existing_feature:
        update_feature = feature_schema.load(feature, session=db.session)
        existing_feature.trail_feature = update_feature.trail_feature
        db.session.merge(existing_feature)
        db.session.commit()
        return feature_schema.dump(existing_feature), 201
    else:
        abort(404, f'Feature with trail feature ID {trail_feature_id} cannot be found')


#Delete
def delete(trail_feature_id):
    existing_feature = Feature.query.filter(Feature.trail_feature_id == trail_feature_id).one_or_none()

    if existing_feature:
        db.session.delete(existing_feature)
        db.session.commit()
        return make_response(f'{trail_feature_id} has been successfully deleted', 200)
    else:
        abort(404, f'Feature with trail feature ID {trail_feature_id} cannot be found')