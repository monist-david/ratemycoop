from django import forms


class SearchForm(forms.Form):
    search_keys = forms.CharField(label='search_keys', max_length=100)
