from tastypie.resources import ModelResource, Resource
from scanapp.models import Device, DeviceSession, ScanSession
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer
from django.core.serializers import json
import json as simplejson
from tastypie import fields
from uuid import uuid4


class PrettyJSONSerializer(Serializer):
    json_indent = 4

    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return simplejson.dumps(data, cls=json.DjangoJSONEncoder, sort_keys=True, ensure_ascii=False, indent=self.json_indent)

class Products(object):

    def __init__(self, *args, **kwargs):
        self.__dict__['_data'] = {}



class DeviceResource(ModelResource):

    new_object = DeviceSession()

    class Meta:
        queryset = Device.objects.all()
        authorization = Authorization()
        allowed_method = ['get','post']
        serializer = PrettyJSONSerializer()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        bundle = super(DeviceResource, self).obj_create(bundle, **kwargs)
        self.new_object.device = bundle.obj
        self.new_object.device_token = uuid4().hex
        self.new_object.save()
        return bundle

    def dehydrate(self, bundle):
        bundle.data = {}
        if bundle.obj.userprofile:
            bundle.data['device_token'] = "error-must log in"
            return bundle
        else:
            bundle.data['device_token'] = self.new_object.device_token
            return bundle


class ProductsResource(Resource):

    # place_name = fields.CharField(attribute='place_name')

    class Meta:
        resource_name = 'products'
        object_class = Products
        authorization = Authorization()
        allowed_method = ['get','post']
        serializer = PrettyJSONSerializer()
        always_return_data = True

    def obj_create(self, bundle, **kwargs):
        new_object = ScanSession()
        new_object.place_name = bundle.data['place_name']
        new_object.save()
        return bundle



