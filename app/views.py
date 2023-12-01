from django.shortcuts import render

# Create your views here.
def home(request):
  context = {
    "num": [1, 2, 3, 4],
    "a": 2,
    "name": "i'm Jai",
    'cut': "String with spaces",
    "empty": "",
    "fruit":  ['Apple', 'Mango', 'Orange'],
    "dic": [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]
,   
  }
  return render(request, 'home.html', context)