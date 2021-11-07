from django.shortcuts import render
from django.views import View

# Create your views here.


class DashboardView(View):
    template_name = "pharmacy/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)
