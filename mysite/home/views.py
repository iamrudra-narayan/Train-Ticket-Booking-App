from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    data = []
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        date = request.POST.get('date')

        url = "https://indian-railway-api.cyclic.app/trains/gettrainon?from="+start+"&to="+end+"&date="+date
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_object = response.json()
        
        for i in range(len(json_object['data'])):
            train_data = json_object['data'][i]['train_base']
            data.append(train_data)

    return render(request, 'home.html', {'data': data})
