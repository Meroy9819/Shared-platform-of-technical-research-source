from django.shortcuts import render
from rest_framework import viewsets, response
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
#from label.models import label
from TechResource.models import Resource
from TechResource.models import SciAchi
from TechResource.models import Inst
from TechResource.serializers import SciAchiSerializer, ResourceSerializer,InstSerializer
from User.serializers import NormalUserSerializer
from User.serializers import ExpertSerializer
from collections import OrderedDict


class SciAchiViewSet(viewsets.ModelViewSet):
    queryset = SciAchi.objects.all()
    serializer_class = SciAchiSerializer

    def create(self, request):
        resource_serializer = ResourceSerializer(data=request.data)
        sciAchi_serializer = SciAchiSerializer(data=request.data)
        if resource_serializer.is_valid():
            if sciAchi_serializer.is_valid():
                thisResource = Resource(
                    name=request.data.get("name"),
                    type="sciAchi"
                )
                thisResource.save()
                thissciAchi = SciAchi(
                    sciAchi=thisResource,
                    sciAchiUrl=request.data.get("path"),
                    abstract=request.data.get("abstract"),
                    keywordSeq=request.data.get("keyword"),
                    price=request.data.get("value"),
                )
                thissciAchi.save()
                return Response(thisResource.resource_id, status=status.HTTP_201_CREATED)
            return Response(sciAchi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(resource_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

    def list(self, request):
        serializer = ResourceSerializer(self.GetQueryset(request), many=True)
        return Response(serializer.data)

    def GetQueryset(self, request):
        name = request.query_params.get('name', None)
        pk = request.query_params.get('pk', None)
        if name is not None:
            queryset = Resource.objects.filter(name__contains=name)
        elif pk is not None:
            queryset = Resource.objects.filter(resource_id=pk)
        else:
            queryset = Resource.objects.all()
        return queryset

    @action(methods=["POST"], detail=False)

    def SearchExpert(self, request):
        pk = request.POST.get("id")
        # return Response(pk, status=status.HTTP_200_OK)
        myresource = Resource.objects.get(resource_id=pk)
        resource_serializer = ResourceSerializer(myresource)

        mypaper = SciAchi.objects.get(paper=pk)
        paper_serializer = SciAchiSerializer(mypaper)

        experts = myresource.expert_set.all()
        serializers = ExpertSerializer(experts, many=True)

        result = serializers.data
        result.append(OrderedDict(resource_serializer.data))
        result.append(OrderedDict(paper_serializer.data))

        return Response(result, status=status.HTTP_200_OK)

   # @action(methods=["POST"], detail=False)


 #   def ResourceLabel(self, request):
  #      my_resource = Resource.objects.get(resource_id=request.data.get("resource_id"))
   #     my_label = label.objects.get(label_id=request.data.get("label_id"))
    #    my_resource.ownlabels.add(my_label)
     #   return Response("ok", status=status.HTTP_200_OK)


class instViewset(viewsets.ModelViewSet):
    queryset = Inst.objects.all()
    serializer_class = InstSerializer

    def create(self, request):
        inst_serializer = InstSerializer(data=request.data)
        if inst_serializer.is_valid():
            thisinst = Inst(name=request.data.get("name"))
            thisinst.save()
            return Response(thisinst.instNum, status=status.HTTP_201_CREATED)
        return Response(Inst.objects.get(name=request.data.get("name")).inst_id,
                        status=status.HTTP_400_BAD_REQUEST)
        inst_serializer = instSerializer(data=request.data)
        resource_serializer = resourceSerializer(data=request.data)
        if resource_serializer.is_valid():
            if inst_serializer.is_valid():
                thisResource = resource(
                    name=request.data.get("name"),
                    type="institution"
                )
                thisResource.save()
                thisinst = inst(
                    inst=thisResource,
                    estaDate=request.data.get("estaDate"),
                )
                thisinst.save()
                return Response(thisinst.inst, status=status.HTTP_201_CREATED)
            return Response(inst.objects.get(name=request.data.get("name")).inst_id,status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = InstSerializer(self.GetQueryset(request), many=True)
        return Response(serializer.data)

    def GetQueryset(self, request):
        name = request.query_params.get('name', None)
        pk = request.query_params.get('pk', None)
        if name is not None:
            queryset = Inst.objects.filter(name__contains=name)
        elif pk is not None:
            queryset = Inst.objects.filter(inst_id=pk)
        else:
            queryset = Inst.objects.all()
        return queryset

    def CreateByApplysheet(applysheet):
        try:
            Inst(
                name=applysheet.name,
            ).save()
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['POST'], detail=False)

    def Search(self, request):
        inst_ = Inst.objects.filter(name=request.data.get("name"))
        return Response(InstSerializer(inst_, many=True).data, status=status.HTTP_200_OK)

    def compare(elem):
        count1 = 0
        queryset_expert = elem.ownexperts.all()
        for expert_in in queryset_expert:
            count1 += expert_in.ownresources.count()
        return count1

    @action(methods=['GET'], detail=False)
    def Rank(self, request):
        rank = []
        queryset_inst = Inst.objects.all()
        for my_inst in queryset_inst:
            my_name = my_inst.name
            count_resource = 0
            queryset_expert = my_inst.ownexperts.all()
            for my_expert in queryset_expert.all():
                count_resource += my_expert.ownresources.count()
            rank.append([my_name, count_resource])
        rank.sort(reverse=True, key=lambda d: d[1])

    @action(methods=["POST"], detail=False)
    def FindResource(self, request):
        rank = []
        queryset_inst = Inst.objects.all()
        for my_inst in queryset_inst:
            queryset_expert = my_inst.ownexperts.all()
            for my_expert in queryset_expert.all():
                my_resource = my_expert.ownresources.all()
                serializers = ResourceSerializer(my_resource, many=True)
                rank.append(serializers.data)
        return Response(rank, status=status.HTTP_200_OK)
