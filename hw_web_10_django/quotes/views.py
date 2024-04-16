from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponse
from django.contrib import messages

from .models import Quote, Tag, Author
from .forms import TagForm, QuoteForm, AuthorForm, AuthorFormList
from .services.gpt_service import generate_random_quote
from .tuning.scraping_migrate import starter_scraping_migration

# Create your views here.


def home_page(request, page=1) :
    only_yours = request.GET.get('flexRadioDefault') == 'yours'

    if only_yours:
        quotes = Quote.objects.filter(user=request.user).order_by('id')
    else:
        quotes = Quote.objects.all().order_by('id')

    elements_page = 10
    paginator = Paginator(quotes, elements_page)
    quotes_one_page = paginator.page(page)

    # Getting the name of the logged-in user
    user_name = request.user.username

    # Count the number of tags in quotes
    tag_counts = Tag.objects.annotate(num_quotes = Count('quote')).order_by('-num_quotes')[:10]

    return render(request, 'quotes/index.html',
                  context = {'quotes' : quotes_one_page, 'only_yours' : only_yours, 'user_name' : user_name,
                             'tag_counts' : tag_counts})


class TagListView(View) :
    def get(self, request) :
        tags = Tag.objects.all()
        return render(request, 'quotes/tags.html', context = {'tags': tags})


class AddTagView(View) :
    def get(self, request) :
        form = TagForm()
        return render(request, 'quotes/add_tag.html', {'form' : form})

    def post(self, request) :
        form = TagForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('quotes:tags')
        return render(request, 'quotes/add_tag.html', {'form' : form})


class EditTagView(View) :
    def get(self, request, tag_id) :
        tag = Tag.objects.get(id = tag_id)
        form = TagForm(instance = tag)
        return render(request, 'quotes/edit_tag.html', {'form' : form})

    def post(self, request, tag_id) :
        tag = Tag.objects.get(id = tag_id)
        form = TagForm(request.POST, instance = tag)
        if form.is_valid() :
            form.save()
            return redirect('quotes:tags')
        return render(request, 'quotes/edit_tag.html', {'form' : form})


class QuoteFormList(View):
    def get(self, request, quote_id=None) :
        if quote_id :
            quote = get_object_or_404(Quote, id = quote_id)
            form = QuoteForm(instance = quote)
        else :
            quote = None
            form = AuthorFormList()
        return render(request, 'quotes/quote_list.html', {'form': form, 'quote': quote})


class QuoteFormView(View) :
    def get(self, request, quote_id=None) :
        # tags = Tag.objects.all()
        if quote_id :
            quote = get_object_or_404(Quote, id = quote_id)
            form = QuoteForm(instance = quote)
        else :
            quote = None
            form = QuoteForm()
        return render(request, 'quotes/quote_form.html', {'form' : form, 'quote' : quote})

    def post(self, request, quote_id=None) :
        # tags = Tag.objects.all()
        if quote_id :
            quote = get_object_or_404(Quote, id = quote_id)
            form = QuoteForm(request.POST, instance = quote)
        else :
            form = QuoteForm(request.POST)
        if form.is_valid() :
            quote = form.save(commit = False)
            quote.save()
            form.save_m2m()
            return redirect('quotes:home')
        return render(request, 'quotes/quote_form.html', {'form' : form})


class QuoteDeleteView(View) :
    def get(self, request, quote_id) :
        quote = get_object_or_404(Quote, id = quote_id)
        return render(request, 'quotes/quote_delete.html', {'quote' : quote})

    def post(self, request, quote_id) :
        quote = get_object_or_404(Quote, id = quote_id)
        quote.delete()
        return redirect('quotes:home')


class AuthorListView(View):
    def get(self, request, author_id=None) :
        if author_id :
            author = get_object_or_404(Author, id = author_id)
            form = AuthorFormList(instance = author)
        else :
            author = None
            form = AuthorFormList()
        return render(request, 'quotes/author.html', {'form': form, 'author': author})


class AuthorFormView(View) :
    def get(self, request, author_id=None) :
        if author_id :
            author = get_object_or_404(Author, id = author_id)
            form = AuthorForm(instance = author)
        else :
            author = None
            form = AuthorForm()
        return render(request, 'quotes/author_form.html', {'form' : form, 'author' : author})

    def post(self, request, author_id=None) :
        if author_id :
            author = get_object_or_404(Author, id = author_id)
            form = AuthorForm(request.POST, instance = author)
        else :
            form = AuthorForm(request.POST)
        if form.is_valid() :
            author = form.save()
            return redirect('quotes:home')
        return render(request, 'quotes/author_form.html', {'form' : form})


class AuthorDeleteView(View) :
    def get(self, request, author_id) :
        author = get_object_or_404(Author, id = author_id)
        return render(request, 'quotes/author_delete.html', {'author' : author})

    def post(self, request, author_id) :
        author = get_object_or_404(Author, id = author_id)
        author.delete()
        return redirect('quotes:home')


class TuningView(View) :
    def get(self, request):
        return render(request, 'quotes/tuning.html', context = {})


class ScrapingView(View) :
    def get(self, request):
        return render(request, 'quotes/scraping.html', context = {})

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
        return render(request, 'quotes/gptchat.html', context = {})

    def post(self, request):
        if 'generate_quote' in request.POST:
            # Call the function to generate a random quote
            quote_message = generate_random_quote(request.user)
            if quote_message==True:
                messages.success(request, 'GPT Chat successfully generated a new entry!')
            else:
                messages.success(request, 'The author database is empty. Fill it up!')
            # Return the message to the same HTML page
            return render(request, 'quotes/gptchat.html', {'quote_message': quote_message})
        else:
            return HttpResponse("Invalid request")
