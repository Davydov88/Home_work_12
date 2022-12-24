def save_pic(picture):
    """Создаем функцию, которая сохраняет картинку и записывает в файл"""
    filename = picture.filename
    type_of_file = filename.split('.')[-1]

    if type_of_file not in ('jpeg', 'jpg', 'bmp', 'svg'):
        return

    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'