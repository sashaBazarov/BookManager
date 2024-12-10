from datetime import datetime
from json import dumps


class Book:

    def __init__(self, id, title: str, author: str, year: datetime, status: str = "In Stock") -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (
            self.id == other.id and
            self.title == other.title and
            self.author == other.author and
            self.year == other.year
        )

    def __hash__(self):
        return hash(self.id)

    @property
    def year(self):
        return self._year.strftime("%Y")

    @year.setter
    def year(self, value):
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%Y")
            except ValueError:
                raise ValueError("Invalid year format.")
        elif not isinstance(value, datetime):
            raise TypeError(
                "Year must be a datetime object or a string in 'YYYY' format.")
        self._year = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    def to_json(self):
        data = self.to_dict()
        return dumps(data, ensure_ascii=False)

    def to_table(self):
        return [self.title, self.author, self.year, 
                self.status, self.id]

    def get_attrs(self):
        return (attr for attr in dir(self) if not callable(getattr(self, attr))
                 and not attr.startswith("__") and not attr.startswith("_") and attr != "id")
