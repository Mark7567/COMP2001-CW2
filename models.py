from config import db, ma
from marshmallow import validates, ValidationError, fields

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    user_id = db.Column(db.String(6), primary_key = True, nullable = False, unique = True)
    email_address = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    role = db.Column(db.String(5), nullable = False)
    username = db.Column(db.String(64), nullable = False)

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
    trail_id = db.Column(db.String(6), primary_key = True, nullable = False, unique = True)
    trail_name = db.Column(db.String(128), nullable = False)
    trail_summary = db.Column(db.String(255), nullable = False)
    trail_description = db.Column(db.String(255), nullable = False)
    difficulty = db.Column(db.String(8), nullable = False)
    location = db.Column(db.String(128), nullable = False)
    length = db.Column(db.Float, nullable = False)
    elevation_gain = db.Column(db.Integer, nullable = False)
    route_type = db.Column(db.String(14), nullable = False)
    owner_id = db.Column(db.String(6), db.ForeignKey('CW2.User.user_id'), nullable = False)
    pt1_lat = db.Column(db.Float, nullable = False)
    pt1_long = db.Column(db.Float, nullable = False)
    pt1_desc = db.Column(db.String(255))
    pt2_lat = db.Column(db.Float, nullable = False)
    pt2_long = db.Column(db.Float, nullable = False)
    pt2_desc = db.Column(db.String(255))
    pt3_lat = db.Column(db.Float, nullable = False)
    pt3_long = db.Column(db.Float, nullable = False)
    pt3_desc = db.Column(db.String(255))
    pt4_lat = db.Column(db.Float, nullable = False)
    pt4_long = db.Column(db.Float, nullable = False)
    pt4_desc = db.Column(db.String(255))
    pt5_lat = db.Column(db.Float, nullable = False)
    pt5_long = db.Column(db.Float, nullable = False)
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
    trail_id = db.Column(db.String(6), db.ForeignKey('CW2.Trail.trail_id'), primary_key = True, nullable = False)
    trail_feature_id = db.Column(db.String(6), db.ForeignKey('CW2.Feature.trail_feature_id'), primary_key = True, nullable = False)

    feature = db.relationship('Feature', backref='trail_features')
    trail = db.relationship('Trail', backref='trail_features')



class Feature(db.Model):
    __tablename__ = 'Feature'
    __table_args__ = {'schema': 'CW2'}
    trail_feature_id = db.Column(db.String(6), primary_key = True, nullable = False, unique = True)
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



class TrailSchema(ma.SQLAlchemyAutoSchema):
    owner_id = fields.Str()
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session


trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance = True
        sqla_session = db.session


feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)


class TrailFeatureSchema(ma.SQLAlchemyAutoSchema):
    trail_id = fields.Str()
    trail_feature_id = fields.Str()
    class Meta:
        model = Trail_Feature
        load_instance = True
        sqla_session = db.session
        


trail_feature_schema = TrailFeatureSchema()
trail_features_schema = TrailFeatureSchema(many=True)