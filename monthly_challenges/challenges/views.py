from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challenges = {
    "january":" Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day!",
    "march":"Eat no meat for entire month",
    "april":"Eat no meat for entire month",
    "may": "Walk for at least 20 minutes every day",
    "june": "walk for at least 20 minutes every day",
    "july":"Eat no meat for entire month",
    "august":"Learn Django for at least 20 minutes every day!",
    "september":"Eat no meat for entire month",
    "october":"Eat no meat for entire month",
    "november":"walk for at least 20 minutes every day!",
    "december":"Eat no meat for entire month"
}
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge",args=[redirect_month]) # /challenges/january

    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1> This month is not supported!</h1>")

