from django.db import models

# Create your models here.
CENSOR_CHOICE = (
    ('C', 'Для детей'),  # c child
    ('G', 'Для взрослых'),  # g grow-up
    ('A', 'Для всех'),  # a all
)


class BookGenre(models.Model):
    genre_book = models.CharField(
        max_length=255,
        help_text='Введите жанр произведения',
        verbose_name='Жанр произведения',
    )

    def __str__(self):
        return self.genre_book


class BookAuthor(models.Model):
    firstName_author = models.CharField(
        max_length=255,
        help_text='Введите имя автора(Обязательно)',
        verbose_name='Имя автора',
        null=True,
    )
    lastName_author = models.CharField(
        max_length=255,
        help_text='Введите фамилию автора(Обязательно)',
        verbose_name='Фамилия автора',
        null=True,
    )

    def __str__(self):
        return self.get_fullname()

    def get_fullname(self) -> str:
        return ' '.join(filter(bool, [self.firstName_author, self.lastName_author]))


class Book(models.Model):
    title_book = models.CharField(
        max_length=255,
        help_text='Введите название произведения(Обязательно)',
        unique=True,
        verbose_name='Название',
    )

    censor = models.CharField(
        max_length=255,
        help_text='Введите тип произведения',
        verbose_name='Цензура',
        choices=CENSOR_CHOICE,
        default=CENSOR_CHOICE[1],
    )

    genre_book = models.ManyToManyField(
        BookGenre, verbose_name='Жанр произведения')

    author = models.ForeignKey(
        BookAuthor, on_delete=models.CASCADE, verbose_name='Имя и фамилия автора')

    content_book = models.TextField(
        help_text='Введите текст произведения(Обязательно)',
        verbose_name='Текст',
    )

    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления',
        null=True
    )

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения',
    )
