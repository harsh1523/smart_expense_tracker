from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer


@api_view(['GET'])
def health_check(request):
    return Response({"status": "Backend running"})

@api_view(['POST'])
def debug_request(request):
    print(request.data)
    return Response({"received": request.data})
    path('debug/', debug_request),
@api_view(['POST'])
def register_user(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User created"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)