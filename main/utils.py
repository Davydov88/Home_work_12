import json


class Postbox():
    """Создаем класс Postbox  с методами"""
    def __int__(self, path):
        self.path = path

    def get_posts(self):
        """Создаем метод, который получает из файла все посты"""
        posts=[]
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
            return posts
        except Exception as e:
            return posts, e
        return posts, None

    def search_posts(self, word):
        """Создаем метод, который ищет по тегу пост"""
        posts = []
        get_posts, error = self.get_posts()
        for post in get_posts:
            if word.lower() in post['content'].lower():
                posts.append(post)
        return posts, error

    def save_post(self, posts):
        """Создаем метод, который записывает новый пост в файл"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        """Создаем метод, который позволяет добавлять новые посты и картинки"""
        posts, error = self.get_posts()
        post.append(post)
        self.save_post(posts)



