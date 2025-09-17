from django.shortcuts import render 
from django.views import View 
from django.http import JsonResponse 
from libs.utils import CoreUtilsMixin 


class IndexView(View):
    template_name = 'core/index.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, status=200)
    

