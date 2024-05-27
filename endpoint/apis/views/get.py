from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from ..serializers import EndpointSerializer, Endpoint
from users.models import Tenant

class user_all_endpoints (APIView) : 
    serializer_class = EndpointSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs) : 
        user = request.user
        tenant = Tenant.objects.get(user=user)
        endpoints = Endpoint.objects.filter(tenant=tenant)
        serializer = self.serializer_class(endpoints, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class user_endpoint (APIView) : 
    
    def get(self, request, tenant, url_route, **kwargs) : 
        try : 
            tenant = Tenant.objects.get(name=tenant)
        except Tenant.DoesNotExist:
            return Response({
                'message' : "tenant not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        try :
            endpoint = Endpoint.objects.get(tenant=tenant, name=url_route)
        except Endpoint.DoesNotExist:
            return Response({
                'message' : "url_router not found"
            },status=status.HTTP_404_NOT_FOUND)
        
        return Response(endpoint.json,status=status.HTTP_200_OK)
