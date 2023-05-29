import django_filters as filters
from books import models
from django.db.models import Q


class BooksFilter(filters.FilterSet):
    title_book = filters.CharFilter(
        label='Поиск по названию книги',
        field_name='title_book',
        lookup_expr='iregex',
        widget=filters.widgets.CSVWidget(
            attrs={'placeholder': 'Поиск по названию книги'}),
    )
    author = filters.CharFilter(
        label='Поиск по автору',
        method='filter_by_author',
        widget=filters.widgets.CSVWidget(
            attrs={'placeholder': 'Поиск по автору книги'}),
    )

    def filter_by_author(self, queryset, name, value):
        return queryset.filter(
            Q(author__firstName_author__iregex=value) | Q(
                author__lastName_author__iregex=value)
        )

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        title_book = self.data.get('title_book')
        author = self.data.get('author')
        if title_book or author:
            queryset = queryset.filter(
                Q(title_book__iregex=title_book) & (
                    Q(author__firstName_author__iregex=author) | Q(
                        author__lastName_author__iregex=author)
                )
            )

        return queryset

    class Meta:
        model = models.Book
        fields = ['title_book',
                  'author',
                  ]
