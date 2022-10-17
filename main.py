import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.json())
d={1:("one","jeden"), 2:("two","dwa")}

print(d.values())
a=(d[1])
print(a[0], a[1])


weather_c={
    "monday":12,
    "thuesday":14,
    "wednesday":15,
    }
weather_f={day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
print(weather_f)
list_of_n=list(a for a in range(1,6))
print(list_of_n)

mydict={a*a for a in list_of_n}
print(mydict)