from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from subprocess import run, PIPE
import sys
from django.shortcuts import render
from django.views import View
from doctor.models import Test
# Create your views here.
import requests
import json
class DashboardView(View):
    template_name = "patient/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
#         headers = {"Content-Type": "application/json;","Authorization":"617bf2eb245383001100f8a6"}
#         sendData = {
#     "phone": "+917044659720",
#     "media": {
#       "type": "media_template",
#       "lang_code": "en",
#       "template_name": "welcome",
#     "body":[

#         {
          
#         }
       
#     ]
      
#     }
#   }
#         jsonObject = json.dumps(sendData)
#         req = requests.post(url = "https://rapidapi.rmlconnect.net/wbm/v1/message",headers=headers, data = jsonObject)
        print("ZWEEEEEEEEEEEEE")

        return render(request, self.template_name)


@csrf_exempt
def heart_beat(request):
    inp = request.POST.get('param')
    out = run([sys.executable, 'C:\\Users\jayit\\Downloads\\RAPID\\MedBay-V1\\HeartRateMonitorGui\\GUI.py'],
              shell=True, stdout=PIPE)
    print(out)
    return render(request, 'patient/dashboard.html', {'data1': out.stdout})


def compare_test(request):

    tests = Test.objects.all().order_by('?')

    return render(request, 'patient/testWeavy.html', {"tests": tests})


@csrf_exempt
def search_tests(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        print(search_text)
    else:
        search_text = ''
    if(search_text == "NONE"):
        print("IN HERE")
        results = Test.objects.all().order_by('?')[:4]
    else:
        print("IN THERE")
        results = Test.objects.filter(
            test_name__contains=search_text, test_name__isnull=False).order_by('test_price')

    return render(None, 'patient/search.html', {"results": results})
