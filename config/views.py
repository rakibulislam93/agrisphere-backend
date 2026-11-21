from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class HomeAPIView(APIView):

    @extend_schema(
        tags=["Root"],
        responses={
            200: {
                "type": "object",
                "properties": {
                    "message": {"type": "string"},
                    "status": {"type": "string"},
                    "server": {"type": "string"},
                    "version": {"type": "string"},
                },
            }
        }
    )
    def get(self, request):
        return Response({
            "message": "Welcome to AgriSphere API",
            "status": "success",
            "server": "running",
            "version": "1.0.0",
        })