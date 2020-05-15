from rest_framework.views import  APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list ot APIView Features"""
        an_apiview = [
            'Uses HTTP methods as funchtion (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
