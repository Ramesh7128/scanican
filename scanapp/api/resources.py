from tastypie.resources import ModelResource
from scanapp.models import Device, DeviceSession
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
        data = {}
        if bundle.obj.userprofile:
            data['device_token'] = "error-must log in"
            return data
        else:
            data['device_token'] = self.new_object.device_token
            return data






