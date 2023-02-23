from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january":"Eat no meat for the entire month",
    "february":"Walk for the entire months",
    "march":"Walk for the entire months",
    "april":"Walk for the entire months",
    "may":"Walk for the entire months",
    "june":"Walk for the entire months",
    "july":"Walk for the entire months",
    "august":"Walk for the entire months",
    "september":"Walk for the entire months",
    "october":"Walk for the entire months",
    "november":"Walk for the entire months",
    "december":"Walk for the entire months",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



# the function below will redirect to monthly_challenges function
def monthly_challenge_by_number(request,month):
    # becuase of keys we can rest that 1 is january and we just count
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    else:
        forward_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[forward_month]) #/challenge
        return HttpResponseRedirect( redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month not supported</h1>")
