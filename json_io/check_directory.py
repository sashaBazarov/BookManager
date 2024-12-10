"""
Этот скрипт обеспечивает существование директории "books/" в текущем рабочем каталоге.
Если директория не существует, она будет создана.

Модули:
    os: Этот модуль предоставляет способ использования функциональности, зависящей от операционной системы.

Функции:
    os.makedirs(name, mode=0o777, exist_ok=False): Эта функция используется для рекурсивного создания директории.
        - name: Имя создаваемой директории.
        - mode: Режим доступа, устанавливаемый для директории.
        - exist_ok: Если True, функция не вызовет исключение, если директория уже существует.
"""
import os
from .books_dirrctory import BOOKS_DIRECTORY


os.makedirs(f"{BOOKS_DIRECTORY}/", exist_ok=True)