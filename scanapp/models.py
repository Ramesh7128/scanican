from django.db import models
from datetime import datetime

# Create your models here.
class Device(models.Model):
    # __tablename__ = 'device'
    # id = models.IntegerField(primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, index=True)
    # device_id = db.Column(db.String(512), index=True)
    # os = db.Column(db.String(128), nullable=True)
    # manufacturer = db.Column(db.String(128), nullable=True)
    # registered_on = db.Column(db.DateTime, default=db.func.now())
    # device_session = db.relationship('DeviceSession', uselist=False, backref='device', lazy='dynamic')
    # scan_sessions = db.relationship('ScanSession', backref='user', lazy='dynamic')

    id = models.IntegerField(primary_key=True) # should id be given??
    user_id = models.IntegerField()
    device_id = models.CharField(max_length=512)
    os = models.CharField(max_length=128, null=True)
    manufacturer = models.CharField(max_length=128, null=True)
    registered_on = models.DateTimeField(default=datetime.now)
    device_session = models.ForeignKey(DeviceSession)
    scan_sessions = models.ForeignKey('ScanSession')


class DeviceSession(models.Model):
    # __tablename__ = 'device_session'
    # id = db.Column(db.Integer, primary_key=True)
    # device_id = db.Column(db.Integer, db.ForeignKey('device.id'), index=True)
    # device_token = db.Column(db.String(512), index=True)
    # new_token = db.Column(db.String(512), nullable=True)
    # is_valid = db.Column(db.Boolean, default=True)
    # issued_date = db.Column(db.DateTime, default=db.func.now())
    # expiry_date = db.Column(db.DateTime, nullable=True)

    # def __init__(self, device_token):
    #     self.device_token = device_token
    #
    # def __repr__(self):
    #     return 'DeviceToken: <device_token: %r, device: %r>' % (self.device_token, self.device)

    id = models.IntegerField(primary_key=True) # id needs to be checked??
    device_id = models.IntegerField()
    device_token = models.CharField(max_length=512)
    new_token = models.CharField(max_length=512, null=True)
    is_valid = models.BooleanField(default=True)
    issued_date = models.DateTimeField(default=datetime.now)
    expiry_date = models.DateTimeField(null=True)


class ScanSession(models.Model):
    # __tablename__ = 'scan_session'
    # id = db.Column(db.Integer, primary_key=True)
    # device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    # place_name = db.Column(db.String(128), nullable=True)
    # latitude = db.Column(db.Float, nullable=True)
    # longitude = db.Column(db.Float, nullable=True)
    # total_scanned = db.Column(db.Integer, default=0)
    # total_matched = db.Column(db.Integer, default=0)
    # total_spent = db.Column(db.Float, default=0.0)
    # total_profit = db.Column(db.Float, default=0.0)
    # session_start = db.Column(db.DateTime, nullable=True)
    # session_end = db.Column(db.DateTime, nullable=True)
    # scan_products = db.relationship('ScannedProduct', backref='scan_session', lazy='dynamic')

    id = models.IntegerField(primary_key=True)
    device_id = models.IntegerField() # cant this made a foreign key to the model
    place_name = models.CharField(max_length=128, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    total_scanned = models.IntegerField(default=0)
    total_matched = models.IntegerField(default=0)
    total_spent = models.FloatField(default=0)
    total_profit = models.FloatField(default=0)
    session_start = models.DateTimeField(null=True)
    session_end = models.DateTimeField(null=True)
    scan_products = models.ForeignKey('ScannedProduct')


class Barcode(db.Model):
    # __tablename__ = 'barcode'
    # id = db.Column(db.Integer, primary_key=True)
    # scan_format = db.Column(db.String(64))
    # scan_code = db.Column(db.String(256))
    # scanned_products = db.relationship('ScannedProduct', backref='barcode', lazy='dynamic')

    scan_format = models.CharField(max_length=64)
    scan_code = models.CharField(max_length=256)
    scanned_products = models.ForeignKey('ScannedProduct')

    # __table_args__ = ( db.UniqueConstraint('scan_format', 'scan_code'),  )
    #
    # def __init__(self, scan_format, scan_code):
    #     self.scan_format = scan_format
    #     self.scan_code = scan_code

class Product(models.Model):
    # __tablename__ = 'product'
    # id = db.Column(db.Integer, primary_key=True)
    # asin = db.Column(db.String(64), index=True)
    # marketplace = db.Column(db.Integer, index=True)
    # title = db.Column(db.String(512), nullable=True)
    # product_type = db.Column(db.String(128), nullable=True)
    # current_sales_rank = db.Column(db.Integer, nullable=True)
    # current_new_price = db.Column(db.Float, nullable=True)
    # current_new_quantity = db.Column(db.Integer, nullable=True)
    # current_used_price = db.Column(db.Float, nullable=True)
    # current_used_quantity = db.Column(db.Integer, nullable=True)
    # last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    # product_history = db.relationship('ProductHistory', backref='product', lazy='dynamic')

    asin = models.CharField(max_length=64)
    marketplace = models.IntegerField()
    title = models.CharField(max_length=512)
    product_type = models.CharField(max_length=128, null=True)
    current_sales_rank = models.IntegerField(null=True)
    current_new_price = models.FloatField(null=True)
    current_new_quantity = models.IntegerField(null=True)
    current_used_price = models.FloatField(null=True)
    current_used_quantity = models.IntegerField(null=True)
    last_updated = models.DateTimeField(default=datetime.now, auto_now_add=True)
    product_history = models.ForeignKey('ProductHistory')

    # def __init__(self, asin, marketplace, title=None, product_type=None):
    #     self.asin = asin
    #     self.marketplace = marketplace
    #     self.title = title
    #     self.product_type = product_type
    #
    # def update_product_history(self, product_history):
    #     self.product_history.append(product_history)
    #     self.current_sales_rank = product_history.sales_rank
    #     self.current_new_price = product_history.new_price
    #     self.current_new_quantity = product_history.new_quantity
    #     self.current_used_price = product_history.used_price
    #     self.current_used_quantity = product_history.used_quantity

class ProductHistory(models.Model):
    #__tablename__ = 'product_history'
    # id = db.Column(db.Integer, primary_key=True)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'), index=True)
    # sales_rank = db.Column(db.Integer, nullable=True)
    # new_price = db.Column(db.Float, nullable=True)
    # new_quantity = db.Column(db.Integer, nullable=True)
    # used_price = db.Column(db.Float, nullable=True)
    # used_quantity = db.Column(db.Integer, nullable=True)
    # added_date = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    # scanned_products = db.relationship('ScannedProduct', backref='product_history', lazy='dynamic')

    product_id = models.ForeignKey('Product')
    sales_rank = models.IntegerField(null=True)
    new_price = models.FloatField(null=True)
    new_quantity = models.IntegerField(null=True)
    used_price = models.FloatField(null=True)
    used_quantity = models.IntegerField(null=True)
    added_data = models.DateTimeField(default= datetime.now, auto_now_add=True) #check on auto_now_add
    scanned_product = models.ForeignKey('ScannedProduct')


class ScannedProduct(models.Model):
    # __tablename__ = 'scanned_product'
    # id = db.Column(db.Integer, primary_key=True)
    # session_id = db.Column(db.Integer, db.ForeignKey('scan_session.id'), index=True)
    # barcode_id = db.Column(db.Integer, db.ForeignKey('barcode.id'), index=True)
    # product_history_id = db.Column(db.Integer, db.ForeignKey('product_history.id'), nullable=True)
    # matched_filter = db.Column(db.Boolean, default=True)
    # scanned_date = db.Column(db.DateTime, nullable=True)

    session_id = models.ForeignKey('ScanSession')
    barcode_id = models.ForeignKey('Barcode')
    product_history_id = models.ForeignKey('ProductHistory')
    matched_filter = models.BooleanField(default=True)
    scanned_date = models.DateTimeField(null=True)