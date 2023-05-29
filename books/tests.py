from django.test import TestCase, Client
from django.urls import reverse
from books import factories


class BookTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.genre_book = factories.BookGenre()
        self.author = factories.BookAuthor()
        self.book = factories.Book(genre_book=self.genre_book)

    def test_list_data(self):
        # Проверяем, что получаем код ответа 200 при запросе к списку книг
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        # Проверяем, что получаем код ответа 200 при запросе деталей конкретной книги
        response = self.client.get(
            reverse('books:book', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)

    def test_about_author(self):
        # Проверяем, что получаем код ответа 200 при запросе информации об авторе
        response = self.client.get(
            reverse('books:book', kwargs={'pk': self.author.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        # Проверяем, что получаем код ответа 302 при удалении книги
        response = self.client.post(
            reverse('books:delete_book', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 302)

    def test_create(self):
        # Проверяем, что получаем код ответа 200 при создании новой книги
        data = {
            'title_book': 'test',
            'censor': 'A',
            'author': self.author,
            'content_book': "HELLO!!",
        }
        data['genre_book'] = [self.genre_book.pk]
        response = self.client.post(
            path=reverse('books:add_book'),
            data=data,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_get_fullname(self):
        # Проверяем, что получаем правильное полное имя автора
        test_fullname = f'{self.author.firstName_author} {self.author.lastName_author}'
        self.assertEqual(self.author.get_fullname(), test_fullname)

    def test_update_book(self):
        # Проверяем, что получаем код ответа 200 при обновлении информации о книге
        data = {
            'title_book': 'test_update',
            'censor': 'A',
            'author': self.author,
            'content_book': "HELLO!! update",
        }
        data['genre_book'] = [self.genre_book.pk]
        response = self.client.post(
            path=reverse('books:update_book',
                         kwargs={'pk': self.book.pk}),
            data=data,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_filter_books_by_genre(self):
        # Проверяем, что получаем код ответа 200 и книга присутствует в результате фильтрации по жанру
        response = self.client.get(
            path=reverse('books:index') + '?genre=' + str(self.genre_book.pk),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title_book)
