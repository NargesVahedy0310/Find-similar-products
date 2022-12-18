from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .models import SearchBox, ValueSearch
from .serializers import SearchBoxSerializer, ValueSearchSerializer
import time
from .google import BotSearch
from rest_framework.response import Response

class GoogelSearchAPI(ModelViewSet):
    serializer_class = SearchBoxSerializer
    def get_queryset(self):
        return SearchBox.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = SearchBoxSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()

        #get data
        data_search = SearchBox.objects.all().values()

        #get data title
        last_data = data_search[::-1][0]
        data_title = last_data['Text_box']
        BotSearch.search_results(data_title, 7)
        return Response(serializer.data)

@api_view()
def ValueSearching(request):
    if request.method == "GET":
        data_search = ValueSearch.objects.all().values()
        last_data = data_search[::-1][0]
        data_title = last_data['title']
        queryset = ValueSearch.objects.filter(title=data_title)
        serializer_class = ValueSearchSerializer(queryset, many=True)
        return Response(serializer_class.data)
