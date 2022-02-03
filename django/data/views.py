from rest_framework import generics

from .models import Data
from .serializers import DataSerializer


class DataListPostView(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()


# 'Retrieve - update - partial update - delete' data by id field
class DataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = "id"
