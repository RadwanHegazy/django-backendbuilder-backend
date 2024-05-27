from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from ..serializers import EndpointSerializer
from users.models import Tenant

class create_endpoint (APIView) : 
    serializer_class = EndpointSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, **kwargs) : 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_200_OK)
