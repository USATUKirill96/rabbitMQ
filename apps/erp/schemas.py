from marshmallow import Schema, fields


class OrderSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    quantity = fields.Int()
    delivery_at = fields.DateTime()
    address = fields.Str()


class TabletOrderSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    quantity = fields.Integer()
    delivery_at = fields.DateTime()


class DriveOrderSchema(Schema):
    id = fields.Integer()
    delivery_at = fields.DateTime()
