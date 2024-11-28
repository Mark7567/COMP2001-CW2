from models import trail_schema, trails_schema, Trail, Trail_Feature
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
        new_trail = trail_schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(406, f'Trail with trail ID {trail_id} already exists')


#Retrieve - Tested - Works as intended
def retrieve(trail_id):
    trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f'Trail with trail ID {trail_id} cannot be found')


#Update Trail Name - Tested - Does not work ---> Allows user to view trail_feature_id (however cannot change it
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


#Update Trail Summary - Not Tested
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


#Update Trail Description - Not Tested
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


#Update Difficulty - Not Tested
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


#Update Location - Not Tested
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
def updatePoint1Latitude(trail_id, trail):
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
def updatePoint1Description(trail_id, trail):
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
def updatePoint2Longitude(trail_id, trail):
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
def updatePoint2Latitude(trail_id, trail):
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
def updatePoint2Description(trail_id, trail):
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
def updatePoint3Longitude(trail_id, trail):
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
def updatePoint3Latitude(trail_id, trail):
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
def updatePoint3Description(trail_id, trail):
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
def updatePoint4Longitude(trail_id, trail):
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
def updatePoint4Latitude(trail_id, trail):
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
def updatePoint4Description(trail_id, trail):
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
def updatePoint5Longitude(trail_id, trail):
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
def updatePoint5Latitude(trail_id, trail):
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
def updatePoint5Description(trail_id, trail):
    existing_trail = Trail.query.filter(Trail.trail_id == trail_id).one_or_none()

    if existing_trail:
        update_trail = trail_schema.load(trail, session=db.session)
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