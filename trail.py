from models import trail_schema, trails_schema, trail_create_schema, Trail, Trail_Feature
from config import db
from flask import make_response, abort

#Reads all entries - Tested - Works as intended
def read_all():
    trail = Trail.query.all()
    return trails_schema.dump(trail)


#Create - Tested - Works as intended
def create(trail):
    trail_id = trail.get("trail_id")
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail is None:
        new_trail = trail_create_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_create_schema.dump(new_trail), 201
    else:
        abort(406, f'Trail with trail ID {trail_id} already exists')


#Retrieve - Tested - Works as intended
def retrieve(trail_id):
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Trail - Tested - Works as intended
def update(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        trail_schema.exclude = ["trail_id"]
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.trail_name = update_trail.trail_name
        existing_trail.trail_summary = update_trail.trail_summary
        existing_trail.trail_description = update_trail.trail_description
        existing_trail.difficulty = update_trail.difficulty
        existing_trail.location = update_trail.location
        existing_trail.length = update_trail.length
        existing_trail.elevation_gain = update_trail.elevation_gain
        existing_trail.route_type = update_trail.route_type
        existing_trail.pt1_long = update_trail.pt1_long
        existing_trail.pt2_long = update_trail.pt2_long
        existing_trail.pt3_long = update_trail.pt3_long
        existing_trail.pt4_long = update_trail.pt4_long
        existing_trail.pt5_long = update_trail.pt5_long
        existing_trail.pt1_lat = update_trail.pt1_lat
        existing_trail.pt2_lat = update_trail.pt2_lat
        existing_trail.pt3_lat = update_trail.pt3_lat
        existing_trail.pt4_lat = update_trail.pt4_lat
        existing_trail.pt5_lat = update_trail.pt5_lat
        existing_trail.pt1_desc = update_trail.pt1_desc
        existing_trail.pt2_desc = update_trail.pt2_desc
        existing_trail.pt3_desc = update_trail.pt3_desc
        existing_trail.pt4_desc = update_trail.pt4_desc
        existing_trail.pt5_desc = update_trail.pt5_desc
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Delete - Tested - Works as intended
def delete(trail_id):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()
    existing_trail_feature = Trail_Feature.query.filter(Trail_Feature.trail_id == trail_id).all()

    if existing_trail:
        for x in existing_trail_feature:
            db.session.delete(x)
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f'{trail_id} has been successfully deleted', 200)
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')