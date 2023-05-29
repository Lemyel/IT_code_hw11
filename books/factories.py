import factory
from faker import Factory
from books import models

factory_ru = Factory.create('ru-Ru')


class BookGenre(factory.django.DjangoModelFactory):
    genre_book = factory_ru.word()

    class Meta:
        model = models.BookGenre


class BookAuthor(factory.django.DjangoModelFactory):
    firstName_author = factory_ru.first_name()
    lastName_author = factory_ru.last_name()

    class Meta:
        model = models.BookAuthor


class Book(factory.django.DjangoModelFactory):
    title_book = factory.Sequence(lambda n: factory_ru.word() + str(n))
    censor = factory_ru.random_element(elements=('C', 'G', 'A'))
    author = factory.SubFactory(BookAuthor)
    content_book = factory_ru.text(max_nb_chars=200)

    @factory.post_generation
    def genre_book(self, create, extracted, **kwargs):
        self.genre_book.add(
            models.BookGenre.objects.create(genre_book="test_genre"))

    class Meta:
        model = models.Book
