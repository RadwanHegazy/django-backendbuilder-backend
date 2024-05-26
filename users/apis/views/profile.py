from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class profile_view (APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request, **kwargs) : 
        user = request.user
        return Response({
            'full_name' : user.full_name,
            'email' : user.email,
        },status=status.HTTP_200_OK)
