from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from index.forms import SearchForm


# Create your views here.


class SearchView(TemplateView):
    template_name = "index/search.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class ManagerView(TemplateView):
    template_name = "index/manager.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)

class PositionView(TemplateView):
    template_name = "index/manager_position.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        return render(request, self.template_name)
