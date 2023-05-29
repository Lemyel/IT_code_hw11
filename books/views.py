
from books import models, forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from books import filters
# Create your views here.


class TitleMixin():
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_title()
        return context


class BookDetail(TitleMixin, DetailView):
    model = models.Book
    template_name = 'books/book.html'
    context_object_name = 'book'
    title = "Содержание книги"


class IndexTemplate(TitleMixin, ListView):
    template_name = 'books/index.html'
    title = "Главная страница"
    model = models.Book
    context_object_name = 'books'

    def get_filters(self):
        return filters.BooksFilter(self.request.GET)

    def get_queryset(self):
        # title_book = self.request.GET.get("title_book")
        # author = self.request.GET.get("author")
        # qs = models.Book.objects.all()
        # if title_book or author:
        #     return qs.filter(
        #             Q(title_book__iregex=title_book) &
        #             (Q(author__firstName_author__iregex=author) |
        #             Q(author__lastName_author__iregex=author))
        #                 )
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = forms.BooksSearch(self.request.GET or None)
        context['filter'] = self.get_filters()
        return context


class AuthorDetail(TitleMixin, DetailView):
    model = models.BookAuthor
    template_name = 'books/about_author.html'
    context_object_name = 'author'
    title = 'Информация об авторе'


class AboutList(TitleMixin, ListView):
    template_name = 'books/about_site.html'
    title = 'О вебсайте'
    model = models.Book


class BookAdd(TitleMixin, CreateView):
    form_class = forms.BookForm

    template_name = 'books/add_book.html'
    title = 'Добавление книги'
    model = models.Book
    success_url = reverse_lazy('books:index')


class BookUpdate(TitleMixin, UpdateView):
    form_class = forms.BookForm

    template_name = 'books/update_book.html'
    title = 'Изменение книги'
    model = models.Book
    success_url = reverse_lazy('books:index')


class BookDelete(TitleMixin, DeleteView):
    model = models.Book
    template_name = 'books/delete_book.html'
    title = 'Удаление книги'
    success_url = reverse_lazy('books:index')
