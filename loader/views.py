from flask import Blueprint, render_template, request, logging

from loader.utils import save_pic
from main.utils import Postbox

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

"""Создаем руты для блюпринта main"""
@loader_blueprint.route("/post")
def new_posts_page():
    return render_template('post_form.html')

@loader_blueprint.route("/post", methods=['POST'])
def add_posts_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Вы заполнили не все поля'

    picture_path =save_pic()
    if not picture_path:
        logging.info('Загружено не изображение!')
        return 'Картинка не загружена'

    post_box = Postbox('posts.json')
    new_post = {'pic': picture_path, 'content': content}
    post_box.add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content )

