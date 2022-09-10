def phoneinfo():
    inp=input("Enter Your Mobile Number with(+91):")
    phone=phonenumbers.parse(inp)
    name=carrier.name_for_number(phone,'en')
    valid=carrier.name_for_valid_number(phone,'en')
    country_name=geocoder.country_name_for_number(phone,'en')
    timezon=timezone.time_zones_for_number(phone)
    print('NAME OF COMPANY:',name,'\n')
    print('NUMBER IS VALID OR NOT:',bool(valid),'\n')
    print('COUNTRY NAME:',country_name,'\n')
    print('TIMEZONE:',timezon,'\n')

def address():
    address=input('Enter Short Address:')
    conv=ArcGIS()
    c=conv.geocode(address)
    lat=c.latitude
    long=c.longitude
    print('Your Complete Address is:',c,'\n')
    print('Your Latitude is:',lat,'\n')
    print('Your Longitude is:',long,'\n')
from phonenumbers import carrier,geocoder,timezone,phonenumberutil
from geopy.geocoders import ArcGIS
import phonenumbers
print('-----------------------PhoneInfoG-----------------------')
print('Developer:Jayant')
print('Press 1:For Finding Phone Number Details')
print('Press 2:For Finding Latitude and logitude Using Address')
print('Press 3:For Quit')
while True:
    press=int(input('Choose:'))
    if(press==1):
        phoneinfo()
    elif(press==2):
        address()
    else:
        break    