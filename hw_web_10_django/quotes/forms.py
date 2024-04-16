from django import forms
from django.forms import CharField, TextInput, Textarea

from .models import Quote, Tag, Author


class TagForm(forms.ModelForm) :
    name = CharField(max_length = 16, min_length = 3, required = True,
                     widget = TextInput(attrs = {"class" : "form-control"}))

    class Meta :
        model = Tag
        fields = ['name']


class QuoteForm(forms.ModelForm) :
    # tags = forms.ModelMultipleChoiceField(queryset = Tag.objects.all(), required = False)

    class Meta :
        model = Quote
        fields = ['author', 'quote', 'tags']
        # exclude = ['tags']


class AuthorForm(forms.ModelForm) :
    # fullname = CharField(max_length = 30, min_length = 5, required = True,
    #                      widget = TextInput(attrs = {"class" : "form-control"}))
    # born_date = CharField(max_length = 50, min_length = 5, required = True,
    #                       widget = TextInput(attrs = {"class" : "form-control"}))
    # born_location = CharField(max_length = 150, min_length = 5, required = True,
    #                           widget = TextInput(attrs = {"class" : "form-control"}))
    # description = CharField(min_length = 5, required = True,
    #                         widget = TextInput(attrs = {"class" : "form-control"}))

    class Meta :
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class AuthorFormList(forms.ModelForm) :

    class Meta :
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']