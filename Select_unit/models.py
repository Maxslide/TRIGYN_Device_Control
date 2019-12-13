from django.db import models

# Create your models here.
class AC(models.Model):
    Ac_name = models.CharField(max_length=255)
    Ac_Latitude = models.CharField(max_length=255)
    Ac_Longitude = models.CharField(max_length=255)
    
class ChangeInAC(models.Model):
    AC_id = models.ForeignKey(AC, on_delete=models.CASCADE)
    current_temp = models.CharField(max_length=10)
    current_fan = models.IntegerField()
    current_swing = models.IntegerField()       
    Name_of_changeMaker = models.CharField(max_length=255)
    
class FAN(models.Model):
    Fan_name = models.CharField(max_length=255)
    Fan_Latitude = models.CharField(max_length=255)
    Fan_Longitude = models.CharField(max_length=255)
    
class ChangeInFAN(models.Model):
    FAN_id = models.ForeignKey(FAN, on_delete=models.CASCADE)
    current_speed = models.IntegerField()
    current_swing = models.IntegerField()       
    Name_of_changeMaker = models.CharField(max_length=255)
    
class Geyser(models.Model):
    Geyser_name = models.CharField(max_length=255)
    Geyser_Latitude = models.CharField(max_length=255)
    Geyser_Longitude = models.CharField(max_length=255)
class ChangeInGeyser(models.Model):
    Geyser_id = models.ForeignKey(Geyser, on_delete=models.CASCADE)
    current_state = models.IntegerField()
    schedule_on_time = models.CharField(max_length=255)
    schedule_off_time = models.CharField(max_length=255)
    follow_schedule_for_week = models.IntegerField()       
    Name_of_changeMaker = models.CharField(max_length=255)
    
class Bulb(models.Model):
    Bulb_name = models.CharField(max_length=255)
    Bulb_Latitude = models.CharField(max_length=255)
    Bulb_Longitude = models.CharField(max_length=255)
class ChangeInBulb(models.Model):
    Bulb_id = models.ForeignKey(Bulb, on_delete=models.CASCADE)
    current_state = models.IntegerField()
    Brightness = models.IntegerField()
    Color = models.CharField(max_length=20)
    Effect = models.IntegerField()       
    Name_of_changeMaker = models.CharField(max_length=255)

class Smart_Wifi(models.Model):
    Wifi_name = models.CharField(max_length=255)
    Wifi_Latitude = models.CharField(max_length=255)
    Wifi_Longitude = models.CharField(max_length=255)
class ChangeInWifi(models.Model):
    Wifi_id = models.ForeignKey(Smart_Wifi, on_delete=models.CASCADE)
    current_state = models.IntegerField()
    NumberOfAllowedConnections = models.IntegerField()
    Bandwidth = models.CharField(max_length=20)       
    Name_of_changeMaker = models.CharField(max_length=255)
    
class Car_Book(models.Model):
    Booking_Name = models.CharField(max_length=255)
    Booked_Value = models.IntegerField()
    Booked_Code = models.CharField(max_length=10)