from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import OrmTestModel
from .serializers import OrmTestModelSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ORM_TEST(APIView):
    def get(self, request, pk=None):
        try:
            if pk:
                try:
                    complex_data = OrmTestModel.objects.get(user_id=pk)
                    serializer = OrmTestModelSerializer(complex_data)
                    
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except OrmTestModel.DoesNotExist:
                    return Response({'error': 'ORMTEST instance not found.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                complex_data = OrmTestModel.objects.all()
                serializer = OrmTestModelSerializer(complex_data, many=True)
                
                return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError:
            return Response({'error': 'Invalid user ID.'}, status=status.HTTP_400_BAD_REQUEST)

