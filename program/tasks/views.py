from django.shortcuts import render

# Create your views here.
tasks=["practicing", "study", "jerking"]

def index(request):
    return render(request,"tasks/index.html", {"tasks":tasks})