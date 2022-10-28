from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from catalog.models import Author, Book


class AuthorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields + ("pseudonym", "first_name", "last_name")


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title.."})
    )
