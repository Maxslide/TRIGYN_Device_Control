from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Select_unit.models import *
import json
from django.core import serializers
# Create your views here.

def index(request):
    return HttpResponse('<h2>Enter the url for which you want the details</h2>')

def devices(request):
    devices = {}
    devices["1"] = "AC"
    devices["2"] = "FAN"
    devices["3"] = "Geyser"
    devices["4"] = "Bulb"
    devices["5"] = "Smart Wifi"
    output = json.dumps(json.loads(json.dumps(devices)),indent=4)
    return HttpResponse(output,content_type='application/json')

def AC_all(request):
    Ac_dev = AC.objects.all()
    bs = {'AC' : Ac_dev}
    # print(bs.objects.all())
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInAC.objects.filter(AC_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Ac_name,
            "Latitude" : i.Ac_Latitude,
            "Longitude" : i.Ac_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

def AC_part(request, ac_id):
    Ac_dev = AC.objects.filter(id = ac_id)
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInAC.objects.filter(AC_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Ac_name,
            "Latitude" : i.Ac_Latitude,
            "Longitude" : i.Ac_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

# For Fan
def Fan_all(request):
    Ac_dev = FAN.objects.all()
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInFAN.objects.filter(FAN_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Fan_name,
            "Latitude" : i.Fan_Latitude,
            "Longitude" : i.Fan_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

def Fan_part(request, ac_id):
    Ac_dev = FAN.objects.filter(id = ac_id)
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInFAN.objects.filter(FAN_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Fan_name,
            "Latitude" : i.Fan_Latitude,
            "Longitude" : i.Fan_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

# For Geyser

def Geyser_all(request):
    Ac_dev = Geyser.objects.all()
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInGeyser.objects.filter(Geyser_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Geyser_name,
            "Latitude" : i.Geyser_Latitude,
            "Longitude" : i.Geyser_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

def Geyser_part(request, ac_id):
    Ac_dev = Geyser.objects.filter(id = ac_id)
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInGeyser.objects.filter(Geyser_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Geyser_name,
            "Latitude" : i.Geyser_Latitude,
            "Longitude" : i.Geyser_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

# For Bulb

def Bulb_all(request):
    Ac_dev = Bulb.objects.all()
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInBulb.objects.filter(Bulb_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Bulb_name,
            "Latitude" : i.Bulb_Latitude,
            "Longitude" : i.Bulb_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

def Bulb_part(request, ac_id):
    Ac_dev = Bulb.objects.filter(id = ac_id)
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInBulb.objects.filter(Bulb_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Bulb_name,
            "Latitude" : i.Bulb_Latitude,
            "Longitude" : i.Bulb_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

# For Wifi

def Wifi_all(request):
    Ac_dev = Smart_Wifi.objects.all()
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInWifi.objects.filter(Wifi_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Wifi_name,
            "Latitude" : i.Wifi_Latitude,
            "Longitude" : i.Wifi_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')

def Wifi_part(request, ac_id):
    Ac_dev = Smart_Wifi.objects.filter(id = ac_id)
    jsonobj = []
    for i in Ac_dev:
        Ac_list = serializers.serialize('json',ChangeInWifi.objects.filter(Wifi_id = i))
        details = {}
        counter = 1
        print(json.loads(Ac_list)[0])
        for j in json.loads(Ac_list):
            details[str(counter)] = j
            counter += 1
        jsonobj.append({
            "ID" : i.pk,
            "Name" : i.Wifi_name,
            "Latitude" : i.Wifi_Latitude,
            "Longitude" : i.Wifi_Longitude,
            "Details" : details
        })
    jsonobj = json.dumps(jsonobj)
    output = json.dumps(json.loads(jsonobj),indent=4)
    return HttpResponse(output,content_type='application/json')