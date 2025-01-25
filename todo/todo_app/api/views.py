from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer,TaskSerializer
from todo_app.models import User,Task

@api_view(['GET'])
def Get_Users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Get_User(request):
    # Retrieve 'id' from query parameters
    user_id = request.GET.get('id')  # Get the 'id' from the query string
    
    if user_id is None:
        return Response({"error": "User ID not provided"}, status=400)
    
    try:
        user = User.objects.get(pk=user_id)  # Fetch the user by the provided ID
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    

@api_view(['POST'])
def Create_User(request):
     data =request.data
     user = User.objects.create(name=data['name'],email=data['email'],password=data['password'])
     
     serializer = UserSerializer(user)
     return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def Update_User(request, pk):
    try:
        # Retrieve the user by primary key (id)
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Pass the user instance and updated data to the serializer
    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
        serializer.save()  # Save the updated user data
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def Delete_User(request, pk):
    try:
        # Retrieve the user by primary key (id)
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        # Return a 404 error if the user does not exist
        return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Delete the user from the database
    user.delete()
    return Response({'message': 'User deleted successfully.'}, status=status.HTTP_200_OK)