from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

from hw_web_10_django.quotes.services.gpt_service import generate_random_quote
from .scraping_migrate import starter_scraping_migration


# Create your views here.

class TuningView(View) :
    def get(self, request):
        return render(request, 'tuning/tuning.html', context = {})


class ScrapingView(View) :
    def get(self, request):
        return render(request, 'tuning/scraping.html', context = {})

    def post(self, request):
        if 'generate_quote' in request.POST:
            # Call the function to generate a random quote
            quote_message = starter_scraping_migration()
            messages.success(request, 'GPT Chat successfully generated a new entry!')
            # Return the message to the same HTML page
            return render(request, 'quotes/scraping.html', {'quote_message': quote_message})
        else:
            return HttpResponse("Invalid request")


class GPTChatView(View) :
    def get(self, request):
        return render(request, 'tuning/gptchat.html', context = {})

    def post(self, request):
        if 'generate_quote' in request.POST:
            # Call the function to generate a random quote
            quote_message = generate_random_quote(request.user)
            messages.success(request, 'GPT Chat successfully generated a new entry!')
            # Return the message to the same HTML page
            return render(request, 'tuning/gptchat.html', {'quote_message': quote_message})
        else:
            return HttpResponse("Invalid request")
