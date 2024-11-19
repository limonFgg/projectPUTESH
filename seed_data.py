'''
Для приложения "Блог для путешественников"
'''

# from main.models import User, Profile, Article, Comment, Like
from django.utils import timezone
from random import randint, choice
from faker import Faker

fake = Faker()

# Создание пользователей и профилей
users = []
for i in range(5):
    user = User.objects.create_user(
        username=f"user{i+1}",
        email=f"user{i+1}@example.com",
        password="password123"
    )
    Profile.objects.create(
        user=user,
        bio=fake.sentence(),
        location=fake.city(),
        profile_picture=None  # Заполните путь, если нужно изображение
    )
    users.append(user)

# Создание статей
articles = []
for i in range(10):
    article = Article.objects.create(
        author=choice(users),
        title=fake.sentence(nb_words=6),
        content=fake.paragraph(nb_sentences=10),
        created_at=timezone.now(),
        cover_image=None  # Заполните путь, если нужно изображение
    )
    articles.append(article)

# Создание комментариев
for i in range(20):
    Comment.objects.create(
        article=choice(articles),
        author=choice(users),
        content=fake.sentence(),
        created_at=timezone.now()
    )

# Создание лайков
for i in range(30):
    try:
        Like.objects.create(
            article=choice(articles),
            user=choice(users),
            created_at=timezone.now()
        )
    except:
        # Если такой лайк уже существует (уникальное ограничение), просто пропускаем
        pass

print("Данные успешно записаны в БД")
