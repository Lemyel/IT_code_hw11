from django import forms
from books import models
import string

# class BooksSearch(forms.Form):
#     title_book = forms.CharField(label='Поиск по названию книги',
#                                 required=False,
#                                 widget=forms.TextInput(attrs={'placeholder': 'Поиск по названию книги'})
#                                 )

#     author = forms.CharField(label='Поиск по автору книги',
#                             required=False,
#                             widget=forms.TextInput(attrs={'placeholder': 'Поиск по автору книги'})
#                             )

#     # def clean_title_book(self):
#     #     title = self.cleaned_data["title_book"]
#     #     if '/' in title:
#     #         raise forms.ValidationError("Имя не должно содержать '/' !")
#     #     return title

#     def clean(self):
#         title = self.cleaned_data.get("title_book")
#         author = self.cleaned_data.get("author")

#         if title and re.search(r"[^/a-zA-Z0-9а-яА-Я\s]", title):
#             raise forms.ValidationError(
#                 "Название книги содержит недопустимые символы, кроме '/'!")

#         if author and re.search(r"[^/a-zA-Z0-9а-яА-Я\s]", author):
#             raise forms.ValidationError(
#                 "Имя автора содержит недопустимые символы!")

#         return title


class BookForm(forms.ModelForm):
    title_book = forms.CharField(label='Название произведения')
    genre_book = forms.ModelMultipleChoiceField(
        label='Жанр произведения',
        queryset=models.BookGenre.objects.all(),
        required=False,
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Book
        fields = '__all__'
        # fields = ('title_book', 'genre', 'content_book')

    # Проверка в названии книги на недопустимые знаки
    def clean_title_book(self):
        title_book = self.cleaned_data['title_book']
        allowed_punctuation = [',', '.', '!', '?', ':', '-', "'", '"']

        for char in title_book:
            if char in string.punctuation and char not in allowed_punctuation:
                raise forms.ValidationError(
                    "Название произведения содержит недопустимые символы пунктуации.")

        return title_book
