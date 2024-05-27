from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import Tenant

class profile_view (APIView) : 
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request, **kwargs) : 
        user = request.user
        tenant = Tenant.objects.get(user=user)
        return Response({
            'id' : str(user.id),
            'full_name' : user.full_name,
            'email' : user.email,
            'tenant' : {
                'name' : tenant.name,
                'id' : str(tenant.id)
            }
        },status=status.HTTP_200_OK)
