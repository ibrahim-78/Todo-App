from rest_framework import serializers  

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name= serializers.CharField(max_length=100)
    email= serializers.EmailField()
    password= serializers.CharField(max_length=50)
    
    def update(self, instance, validated_data):
        # Update the instance with the new data
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)  # Hash the password if needed
        instance.save()  # Save the updated instance
        return instance

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    isdone = serializers.BooleanField(default=False)
    user = UserSerializer()
 