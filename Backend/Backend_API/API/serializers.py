from rest_framework import serializers
# from Users.models import User

# #  Defines what gets serialized and deserialized 
# class LoginUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username','password']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username','email_address','password','tile',
#         'first_name','surname','cell_number','date_of_birth','gender','primary_address',
#         'city','postal_code','country','citizenship']

# class RemoveUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']

# USAGE
# Serializer must inherit from this class 
# e.g. UserSerializer(user, fields=('id', 'email'))
class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
