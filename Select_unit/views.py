from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from geopy.geocoders import Nominatim
# Create your views here.

geolocator = Nominatim(user_agent="specify_your_app_name_here")

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def ac_page(request):
    all_AC = AC.objects.all()
    context = {'all_AC': all_AC}
    return render(request, 'AC.html', context)


def ac_change(request, ac_id):
    al_AC = ChangeInAC.objects.filter(AC_id=AC.objects.filter(id=ac_id)[0])
    ACobj = AC.objects.filter(id=ac_id)[0]
    newlist = []
    newlist.append(ACobj.Ac_Latitude)
    newlist.append(",")
    newlist.append(ACobj.Ac_Longitude)
    location = geolocator.reverse("".join(newlist))
    context = {'all_AC': al_AC,
                'location' : location
               }
    return render(request, 'AC_change.html', context)


def ac_makechange(request, acch_id):
    if request.method == 'POST':
        print(request.POST.get('Temp'))
        print(request.POST.get('Fan_speed'))
        print(request.POST.get('Swing'))
        print(request.POST.get('Name'))
        print(request.POST.get('acId'))
        post = ChangeInAC()
        post.current_temp = request.POST.get('Temp')
        post.current_fan = int(request.POST.get('Fan_speed'))
        print(request.POST.get('Fan_speed'))
        post.current_swing = int(request.POST.get('Swing'))
        post.Name_of_changeMaker = request.POST.get('Name')
        post.AC_id = AC.objects.filter(id=int(request.POST.get('acId')))[0]
        post.save()
        al_AC = ChangeInAC.objects.filter(
            AC_id=AC.objects.filter(id=(int(request.POST.get('acId'))))[0])
        context = {'all_AC': acch_id}
        return render(request, 'MakeChange.html', context)
    context = {'all_AC': acch_id}
    return render(request, 'MakeChange.html', context)


# FOR FAN NOW

def FAN_page(request):
    all_AC = FAN.objects.all()
    context = {'all_AC': all_AC}
    return render(request, 'FAN.html', context)


def fan_change(request, ac_id):
    al_AC = ChangeInFAN.objects.filter(FAN_id=FAN.objects.filter(id=ac_id)[0])
    context = {'all_AC': al_AC}
    return render(request, 'FAN_change.html', context)


def fan_makechange(request, acch_id):
    if request.method == 'POST':
        post = ChangeInFAN()
        # post.current_temp = request.POST.get('Temp')
        post.current_speed = int(request.POST.get('Fan_speed'))
        post.current_swing = int(request.POST.get('Swing'))
        post.Name_of_changeMaker = request.POST.get('Name')
        post.FAN_id = FAN.objects.filter(id=int(request.POST.get('acId')))[0]
        post.save()
        al_AC = ChangeInFAN.objects.filter(
            FAN_id=FAN.objects.filter(id=(int(request.POST.get('acId'))))[0])
        context = {'all_AC': acch_id}
        return render(request, 'Fan_MakeChange.html', context)
    context = {'all_AC': acch_id}
    return render(request, 'Fan_MakeChange.html', context)

# For Geyser


def Geyser_page(request):
    all_AC = Geyser.objects.all()
    context = {'all_AC': all_AC}
    return render(request, 'Geyser.html', context)


def Geyser_change(request, ac_id):
    al_AC = ChangeInGeyser.objects.filter(Geyser_id=Geyser.objects.filter(id=ac_id)[0])
    context = {'all_AC': al_AC}
    return render(request, 'Geyser_change.html', context)


def Geyser_makechange(request, acch_id):
    if request.method == 'POST':
        post = ChangeInGeyser()
        # post.current_temp = request.POST.get('Temp')
        post.current_state = int(request.POST.get('State'))
        post.schedule_on_time = request.POST.get('schedule_on')
        post.schedule_off_time = request.POST.get('schedule_off')
        post.follow_schedule_for_week=request.POST.get('week')
        post.Name_of_changeMaker=request.POST.get('Name')
        post.Geyser_id=Geyser.objects.filter(
            id=int(request.POST.get('acId')))[0]
        post.save()
        al_AC=ChangeInGeyser.objects.filter(
            Geyser_id=Geyser.objects.filter(id=(int(request.POST.get('acId'))))[0])
        context={'all_AC': acch_id}
        return render(request, 'Geyser_MakeChange.html', context)
    context={'all_AC': acch_id}
    return render(request, 'Geyser_MakeChange.html', context)


# For bulb


def Bulb_page(request):
    all_AC = Bulb.objects.all()
    context = {'all_AC': all_AC}
    return render(request, 'Bulb.html', context)


def Bulb_change(request, ac_id):
    al_AC = ChangeInBulb.objects.filter(Bulb_id=Bulb.objects.filter(id=ac_id)[0])
    ACobj = Bulb.objects.filter(id=ac_id)[0]
    newlist = []
    newlist.append(ACobj.Bulb_Latitude)
    newlist.append(",")
    newlist.append(ACobj.Bulb_Longitude)
    location = geolocator.reverse("".join(newlist))
    context = {'all_AC': al_AC,
                'location' : location
               }
    return render(request, 'Bulb_change.html', context)


def Bulb_makechange(request, acch_id):
    if request.method == 'POST':
        post = ChangeInBulb()
        # post.current_temp = request.POST.get('Temp')
        post.current_state = int(request.POST.get('State'))
        post.Color = request.POST.get('Color')
        post.Brightness = int(request.POST.get('Brightness'))
        post.Effect=int(request.POST.get('Effect'))
        post.Name_of_changeMaker=request.POST.get('Name')
        post.Bulb_id=Bulb.objects.filter(id=int(request.POST.get('acId')))[0]
        post.save()
        al_AC=ChangeInBulb.objects.filter(Bulb_id=Bulb.objects.filter(id=(int(request.POST.get('acId'))))[0])
        context={'all_AC': acch_id}
        return render(request, 'Bulb_MakeChange.html', context)
    context={'all_AC': acch_id}
    return render(request, 'Bulb_MakeChange.html', context)


# for smart wifi

def Wifi_page(request):
    all_AC = Smart_Wifi.objects.all()
    context = {'all_AC': all_AC}
    return render(request, 'Wifi.html', context)


def Wifi_change(request, ac_id):
    al_AC = ChangeInWifi.objects.filter(Wifi_id=Smart_Wifi.objects.filter(id=ac_id)[0])
    context = {'all_AC': al_AC}
    return render(request, 'Wifi_change.html', context)


def Wifi_makechange(request, acch_id):
    if request.method == 'POST':
        post = ChangeInWifi()
        # post.current_temp = request.POST.get('Temp')
        post.current_state = int(request.POST.get('State'))
        post.NumberOfAllowedConnections = int(request.POST.get('Allowed'))
        post.Bandwidth = int(request.POST.get('bandwidth'))
        post.Name_of_changeMaker=request.POST.get('Name')
        post.Wifi_id=Smart_Wifi.objects.filter(id=int(request.POST.get('acId')))[0]
        post.save()
        al_AC=ChangeInWifi.objects.filter(Wifi_id=Smart_Wifi.objects.filter(id=(int(request.POST.get('acId'))))[0])
        context={'all_AC': acch_id}
        return render(request, 'Wifi_MakeChange.html', context)
    context={'all_AC': acch_id}
    return render(request, 'Wifi_MakeChange.html', context)

#Fro car parking

def Car_Park_page(request):
    context = {}
    return render(request,'Car_park.html',context)

def Car_book(request):
    
    if request.method == 'POST':
        Book = Car_Book.objects.all()
        newBook = ""
        print(Book)
        for i in Book:
            newBook = i
            print(newBook)
        post = Car_Book()   
        book_code = int(request.POST.get('booking'))
        temp = list(newBook.Booked_Code)
        temp[book_code - 1] = '1'
        newBook = "".join(temp)
        post.Booked_Value = book_code
        post.Booked_Code = newBook
        post.Booking_Name = request.POST.get('Name')
        post.save()
        Book = Car_Book.objects.all()
        newBook = ""
        print(Book)
        for i in Book:
            newBook = i
            print(newBook)
        context = {'Book_Display' : str(newBook.Booked_Code)}
        return render(request, 'Car_Book.html', context)
    Book = Car_Book.objects.all()
    newBook = ""
    print(Book)
    for i in Book:
        newBook = i
        print(newBook)
    context = {'Book_Display' : str(newBook.Booked_Code)}
    return render(request, 'Car_Book.html', context)
    
def Car_remove(request):
    
    if request.method == 'POST':
        Book = Car_Book.objects.all()
        newBook = ""
        print(Book)
        for i in Book:
            newBook = i
            print(newBook)
        post = Car_Book()   
        book_code = int(request.POST.get('booking'))
        temp = list(newBook.Booked_Code)
        temp[book_code - 1] = '0'
        newBook = "".join(temp)
        post.Booked_Value = book_code
        post.Booked_Code = newBook
        post.Booking_Name = request.POST.get('Name')
        post.save()
        Book = Car_Book.objects.all()
        newBook = ""
        print(Book)
        for i in Book:
            newBook = i
            print(newBook)
        context = {'Book_Display' : str(newBook.Booked_Code)}
        return render(request, 'Car_remove.html', context)
    Book = Car_Book.objects.all()
    newBook = ""
    print(Book)
    for i in Book:
        newBook = i
        print(newBook)
    context = {'Book_Display' : str(newBook.Booked_Code)}
    return render(request, 'Car_remove.html', context)