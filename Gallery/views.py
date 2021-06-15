# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Lottery 

class IndexView(generic.ListView):
    template_name = 'Gallery/index.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Lottery.objects.all()[:8]

