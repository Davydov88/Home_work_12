from flask import Blueprint, render_template, request
import logging
from main.utils import Postbox

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

"""Создаем руты для блюпринта main"""
@main_blueprint.route("/")
def main_page():
    return render_template('index.html')


@main_blueprint.route("/search", methods=['GET'])
def search_page():
    word = request.args.get('s')
    logging.info(f'Поиск: {word}')
    post_box = Postbox('posts.json')
    posts, error = post_box.get_posts(word)
    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка'
    return render_template('post_list.html', posts=posts, word=word)
