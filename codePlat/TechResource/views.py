from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
#from label.models import label
from TechResource.models import SciAchi
from TechResource.serializers import SciAchiSerializer
from User.serializers import NormalUserSerializer
from User.serializers import ExpertSerializer
from collections import OrderedDict
from django.shortcuts import render, get_object_or_404,render_to_response




class SciAchiViewSet(viewsets.ModelViewSet):
    queryset = SciAchi.objects.all()
    serializer_class = SciAchiSerializer

    def list_all(request):
        # queryset = SciAchi.objects.all()
        #  queryset = [12, 23, 4, 5]
        # return render(request, 'testResource.html', {'data': queryset})
        data = SciAchi.objects.all()
        return render(request, 'techResource.html', {'data': data})
    def list_one(request,resource_id):
        data=get_object_or_404(SciAchi,resource_id=resource_id)
        return render(request, 'techDetail.html', {'data': data})




    def create(self, request):
        sciAchi_serializer = SciAchiSerializer(data=request.data)
        if sciAchi_serializer.is_valid():
            thissciAchi = SciAchi(
                name=request.data.get("name"),
                sciAchiUrl=request.data.get("path"),
                abstract=request.data.get("abstract"),
                keywordSeq=request.data.get("keyword"),
                price=request.data.get("value"),
             )
            thissciAchi.save()
            return Response(thissciAchi.resource_id, status=status.HTTP_201_CREATED)
        return Response(sciAchi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = SciAchiSerializer(self.GetQueryset(request), many=True)
        return Response(serializer.data)

    def GetQueryset(self, request):
        name = request.query_params.get('name', None)
        pk = request.query_params.get('pk', None)
        if name is not None:
            queryset = SciAchi.objects.filter(name__contains=name)
        elif pk is not None:
            queryset =  SciAchi.objects.filter(resource_id=pk)
        else:
            queryset =  SciAchi.objects.all()
        return queryset


   # @action(methods=["POST"], detail=False)


 #   def ResourceLabel(self, request):
  #      my_resource = Resource.objects.get(resource_id=request.data.get("resource_id"))
   #     my_label = label.objects.get(label_id=request.data.get("label_id"))
    #    my_resource.ownlabels.add(my_label)
     #   return Response("ok", status=status.HTTP_200_OK)
