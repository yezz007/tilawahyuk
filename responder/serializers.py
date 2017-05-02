from .models import Organization, User, Group
from rest_framework import serializers



class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value

class UserSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	user_id = serializers.CharField(max_length=256)
	register_date = serializers.DateTimeField()
	name = serializers.CharField(max_length=32)
	tilawah_count = serializers.IntegerField(default=0)
	tilawah_miss = serializers.IntegerField(default=0)
	tilawah_day = JSONSerializerField()
	class Meta:
		model = User
		fields = ('id', 'name', 'user_id', 'register_date', 'tilawah_count', 'tilawah_miss', 'tilawah_day')


class GroupSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	group_id = serializers.CharField(max_length=256)
	register_date = serializers.DateTimeField()
	name = serializers.CharField(max_length=32)
	user_count = serializers.IntegerField(default=0)
	user_set = UserSerializer(many=True)
	class Meta:
		model = Group
		fields = ('name', 'group_id', 'register_date', 'user_count', 'id', 'user_set')

class OrganizationSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	created = serializers.DateTimeField()
	name = serializers.CharField(max_length=128)
	register_token = serializers.CharField(max_length=8) #used for adding users
	group_count = serializers.IntegerField(default=0)
	group_set = GroupSerializer(many=True)
	class Meta:
		model = Organization
		fields = ('name', 'register_token', 'created', 'group_count', 'id', 'group_set')