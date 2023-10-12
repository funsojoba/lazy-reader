from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    uid = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=False)
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class UsernameSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)


class SetUsernameSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(request=True)