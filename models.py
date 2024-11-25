from config import db, ma
from marshmallow import validates, ValidationError

class User(db.Model):
    __tablename__ = '[User]'
    __table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.String(6), primary_key = True)
    email_address = db.Column(db.String(50))
    password = db.Column(db.String(20))
    role = db.Column(db.String(5))

    @validates('user_id')
    def validate_user_id(self, value):
        letters = value.substring(0, 1)
        numbers = value.substring(2, 5)
        if len(value) != 6:
            raise ValidationError('Error: User ID must be 6 characters')
        if letters != 'UR':
            raise ValidationError('Error: User ID must start with UR')
        if numbers.isdigit() == False:
            raise ValidationError('Error: User ID must end with 4 letters')

    @validates('email_address')
    def validate_email_address(self, value):
        if '@' not in value and '.' not in value:
            raise ValidationError('Error: Invalid email address')

    @validates('role')
    def validate_role(self, value):
        if value != 'user' or value != 'owner':
            raise ValidationError('Error: Invalid role type - Must be user or owner')



class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    trail_id = db.Column(db.String(6), primary_key = True)
    trail_name = db.Column(db.String(128))
    trail_summary = db.Column(db.String(255))
    trail_description = db.Column(db.String(255))
    difficulty = db.Column(db.String(8))
    location = db.Column(db.String(128))
    length = db.Column(db.Float)
    elevation_gain = db.Column(db.Int)
    route_type = db.Column(db.String(14))
    owner_id = db.Column(db.String(6))
    pt1_lat = db.Column(db.Float)
    pt1_long = db.Column(db.Float)
    pt1_desc = db.Column(db.String(255))
    pt2_lat = db.Column(db.Float)
    pt2_long = db.Column(db.Float)
    pt2_desc = db.Column(db.String(255))
    pt3_lat = db.Column(db.Float)
    pt3_long = db.Column(db.Float)
    pt3_desc = db.Column(db.String(255))
    pt4_lat = db.Column(db.Float)
    pt4_long = db.Column(db.Float)
    pt4_desc = db.Column(db.String(255))
    pt5_lat = db.Column(db.Float)
    pt5_long = db.Column(db.Float)
    pt5_desc = db.Column(db.String(255))

    @validates('trail_id')
    def validate_trail_id(self, value):
        letters = value.substring(0, 1)
        numbers = value.substring(2, 5)
        if len(value) != 6:
            raise ValidationError('Error: Trail ID must be 6 characters')
        if letters != 'UR':
            raise ValidationError('Error: Trail ID must start with TR')
        if numbers.isdigit() == False:
            raise ValidationError('Error: Trail ID must end with 4 letters')

    @validates('difficulty')
    def validate_difficulty(self, value):
        if value != 'Easy' or value != 'Moderate' or value != 'Hard':
            raise ValidationError('Error: Invalid difficulty - Must be easy, moderate, or hard')

    @validates('length')
    def validate_length(self, value):
        if value <= 0.0 or value > 999.9:
            raise ValidationError('Error: Invaid trail length - Must be between 0.0 and 1000.0')

    @validates('elevation_gain')
    def validate_elevation_gain(self, value):
        if value < 0 or value > 99999:
            raise ValidationError('Error: Invalid elevation gain - Must be between 0 and 99999')

    @validates('route_type')
    def validate_route_type(self, value):
        if value != 'Loop' or value != 'Out and Back' or value != 'Point to Point':
            raise ValidationError('Error: Invalid route type - Must be loop, out and back, or point to point')
        
    @validates('pt1_lat')
    def validate_pt1_lat(self, value):
        if value <= -90.0 or value >= 90.0:
            raise ValidationError('Error: Invalid latitude - Must be between -90 and 90') 

    @validates('pt1_long')
    def validate_pt1_long(self, value):
        if value <= -180.0 or value >= 180.0:
            raise ValidationError('Error: Invalid latitude - Must be between -180 and 180')
        
    @validates('pt2_lat')
    def validate_pt2_lat(self, value):
        if value <= -90.0 or value >= 90.0:
            raise ValidationError('Error: Invalid latitude - Must be between -90 and 90')
        
    @validates('pt2_long')
    def validate_pt2_long(self, value):
        if value <= -180.0 or value >= 180.0:
            raise ValidationError('Error: Invalid latitude - Must be between -180 and 180')
        
    @validates('pt3_lat')
    def validate_pt3_lat(self, value):
        if value <= -90.0 or value >= 90.0:
            raise ValidationError('Error: Invalid latitude - Must be between -90 and 90')
        
    @validates('pt3_long')
    def validate_pt3_long(self, value):
        if value <= -180.0 or value >= 180.0:
            raise ValidationError('Error: Invalid latitude - Must be between -180 and 180')
        
    @validates('pt4_lat')
    def validate_pt4_lat(self, value):
        if value <= -90.0 or value >= 90.0:
            raise ValidationError('Error: Invalid latitude - Must be between -90 and 90')
        
    @validates('pt4_long')
    def validate_pt4_long(self, value):
        if value <= -180.0 or value >= 180.0:
            raise ValidationError('Error: Invalid latitude - Must be between -180 and 180')
        
    @validates('pt5_lat')
    def validate_pt5_lat(self, value):
        if value <= -90.0 or value >= 90.0:
            raise ValidationError('Error: Invalid latitude - Must be between -90 and 90')
        
    @validates('pt5_long')
    def validate_pt5_long(self, value):
        if value <= -180.0 or value >= 180.0:
            raise ValidationError('Error: Invalid latitude - Must be between -180 and 180')



class Trail_Feature(db.Model):
    __tablename__ = 'Trail_Feature'
    __table_args__ = {'schema': 'CW2'}
    trail_id = db.Column(db.String(6), primary_key = True)
    trail_feature_id = db.Column(db.String(6), primary_key = True)



class Feature(db.Model):
    __tablename__ = 'Feature'
    __table_args__ = {'schema': 'CW2'}
    trail_feature_id = db.Column(db.String(6), primary_key = True)
    trail_feature = db.Column(db.String(255))

    @validates('trail_feature_id')
    def validate_trail_feature_id(self, value):
        letters = value.substring(0, 1)
        numbers = value.substring(2, 5)
        if len(value) != 6:
            raise ValidationError('Error: Trail Feature ID must be 6 characters')
        if letters != 'UR':
            raise ValidationError('Error: Trail Feature ID must start with TF')
        if numbers.isdigit() == False:
            raise ValidationError('Error: Trail Feature ID must end with 4 letters')