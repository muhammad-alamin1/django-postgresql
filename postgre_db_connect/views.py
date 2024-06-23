from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ConnectDB
from .serializers import ConnectDBSerializers


@method_decorator(csrf_exempt, name='dispatch')
class Connect(APIView):
    # get all dataset or specific data by pk
    def get(self, request, pk=None):
        try:
            if pk:
                complex_data = ConnectDB.objects.get(user_id=pk)
                serializers = ConnectDBSerializers(complex_data)
                
                return Response(serializers.data, status=status.HTTP_200_OK)
            else:
                complex_data = ConnectDB.objects.all()
                serializers = ConnectDBSerializers(complex_data, many=True)
                
                return Response(serializers.data, status=status.HTTP_200_OK)
        except ConnectDB.DoesNotExist:
            return Response({ 'error': 'ConnectDB instance not found.!'}, content_type='application/json', status=status.HTTP_404_NOT_FOUND)


class RootPage(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root_page_data = "This is root page"
        
    def get(self, request):
        return HttpResponse(self.root_page_data, content_type='application/json')
    