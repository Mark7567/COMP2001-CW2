from models import trail_schema, trails_schema, Trail
from config import db
from flask import make_response, abort

def read_all():
    trail = Trail.query.all()
    return trails_schema.dump(trail)


#Create
def create(trail):
    trail_id = trail.get("trail_id")
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail is None:
        new_trail = trail_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f'Trail with trail ID {trail_id} already exists')


#Retrieve
def retrieve(trail_id):
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_more()

    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Trail Name
def updateTrailName(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.trail_name = update_trail.trail_name
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Trail Summary
def updateTrailSummary(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.trail_summary = update_trail.trail_summary
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Trail Description
def updateTrailDescription(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.trail_description = update_trail.trail_description
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Difficulty
def updateDifficulty(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.difficulty = update_trail.difficulty
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Location
def updateLocation(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.location = update_trail.location
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Length
def updateLength(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.length = update_trail.length
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Elevation Gain
def updateElevationGain(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.elevation_gain = update_trail.elevation_gain
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Route Type
def updateRouteType(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.route_type = update_trail.route_type
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 1 Longitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt1_long = update_trail.pt1_long
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 1 Latitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt1_lat = update_trail.pt1_lat
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 1 Description
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt1_desc = update_trail.pt1_desc
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 2 Longitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt2_long = update_trail.pt2_long
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 2 Latitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt2_lat = update_trail.pt2_lat
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 2 Description
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt2_desc = update_trail.pt2_desc
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 3 Longitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt3_long = update_trail.pt3_long
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 3 Latitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt3_lat = update_trail.pt3_lat
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 3 Description
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt3_desc = update_trail.pt3_desc
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 4 Longitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt4_long = update_trail.pt4_long
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 4 Latitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt4_lat = update_trail.pt4_lat
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 4 Description
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt4_desc = update_trail.pt4_desc
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 5 Longitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt5_long = update_trail.pt5_long
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 5 Latitude
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt5_lat = update_trail.pt5_lat
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Point 5 Description
def updatePoint1Longitude(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
        existing_trail.pt5_desc = update_trail.pt5_desc
        db.session.merge(existing_trail)
        db.session.commit()
        return trail_schema.dump(existing_trail), 201
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Delete
def delete(trail_id):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        db.session.delete(existing_trail)
        db.session.commit()
        return make_response(f'{trail_id} has been successfully deleted', 200)
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')