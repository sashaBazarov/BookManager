import commands

def load_command(command: str):
    """
    Загрузите соответствующую функцию для данной командной строки.

    Аргументы:
        command (str): Командная строка для загрузки функции.

    Возвращает:
        function: Функция, соответствующая данной командной строке, или None, если команда не распознана.
    """
    return {
        "books": commands.view_books,
        "addbook": commands.add_book,
        "editbook": commands.edit_book,
        "clear": commands.clear,
        "exit": exit,
        "del": commands.remove_book,
        "help": commands.help
    }.get(command)
