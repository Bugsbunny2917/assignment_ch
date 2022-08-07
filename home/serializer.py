from rest_framework import serializers

from .models import Todo

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','gender','name','email','dob','phone','cell','nat','age']
    # def validate(self, validate_data):
    #     print(validate_data)
    #     return validate_data
        # return super().validate(validate_data)