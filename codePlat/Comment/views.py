from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets, response
from TechResource.models import SciAchi
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import CommentsForm
# Create your views here.
