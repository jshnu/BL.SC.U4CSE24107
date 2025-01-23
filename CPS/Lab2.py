#Question 1
print("Monthly Pay Calculator")
hr=int(input("Enter the number of hours worked in a week by the employee:"))
rate=float(input("Enter the rate per hour:"))
monthly_pay=hr*rate*4.345 # Assuming 4.345 weeks per month
print()
print("The Monthly Pay of the employee is:",monthly_pay,"rs")
print()

#Question 2
from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic
import requests

print("###### Road Trip Distance calculator and Cost Estimator #######")
print()
F_cost=float(input("Enter the cost of fuel (in rs):"))
mileage=float(input("Enter the average mileage of the car (km/l):"))

key = '<Enter your own OpenCage API key here>'
try:
    geocoder = OpenCageGeocode(key)

    A = input("Enter Starting point of road trip:")
    B = input("Enter Ending point of road trip:")
    print()

    result_A = geocoder.geocode(A)
    lat_A = result_A[0]['geometry']['lat']
    lng_A = result_A[0]['geometry']['lng']
    result_B = geocoder.geocode(B)
    lat_B = result_B[0]['geometry']['lat']
    lng_B = result_B[0]['geometry']['lng']

    origin = '{},{}'.format(lat_A,lng_A)
    destination = '{},{}'.format(lat_B,lng_B)  

    API_KEY = '<Enter your own HERE API key here>'
    url = f'https://router.hereapi.com/v8/routes'

    params = {
        'apikey': API_KEY,
        'transportMode': 'car',
        'origin': origin,        
        'destination': destination,  
        'return': 'summary',    
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        distance = data['routes'][0]['sections'][0]['summary']['length']
        distance_km = distance / 1000.0
        travel_time_seconds = data['routes'][0]['sections'][0]['summary']['duration']
        travel_time_hours = "{} hr {} min".format(travel_time_seconds//3600,(travel_time_seconds%3600)//60)
        print("The Distance Between {} And {} Is {} Kilometers.".format(A,B,int(distance_km)))
        print("The Time Required To Travel Is {}.".format(travel_time_hours))
        print("The Fuel Cost Is",round(F_cost*(distance_km/mileage),2),"rs")
    else:
        print(f"Error: {response.status_code}, {response.text}")
    print()
except:
    print()
    print("### ERROR: SET YOUR OWN API ###")
    print()

#Question 3
T=float(input("Enter the temperature in Fahrenheit (°F): "))
Tc=(5/9)*(T-32)
print("Temperature in Celsius (°F): ",Tc)
print()

#Question 4
print("Seconds to HH:MM:SS format")
s=int(input("Enter the time in seconds (interger):"))
print("Time in HH:MM:SS is",s//3600,":",(s%3600)//60,":",(s%3600)%60)
print()

#Question 5
print("Speed Calculator")
d=float(input("Enter the distance travelled (in meters):"))
t=float(input("Enter the time taken (in seconds):"))
speed=d/t
print("Speed in m/s =",speed)
print("Speed in km/hr =",speed*3.6)

