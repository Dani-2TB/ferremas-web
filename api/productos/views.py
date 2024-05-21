from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductosRoot(APIView):
    def get(self, request):
        return Response({"detail":"Esta es la raiz del endpoint: productos"},status.HTTP_200_OK)