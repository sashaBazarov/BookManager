def generate_table(data: list, headers: list = None):
    if not data:
        return "No data available."

    if headers:
        data = [headers] + data

    # Вычисление ширины каждого столбца
    column_widths = [
        max(len(str(row[i]) if i < len(row) else "") for row in data)
        for i in range(len(data[0]))
    ]

    def format_row(row):
        # Форматирование строки с учетом ширины столбцов
        return " | ".join(str(row[i]).ljust(column_widths[i]) if i < len(row) else "".ljust(column_widths[i]) for i in range(len(column_widths)))

    table = []
    table.append(format_row(data[0]))  # Заголовок
    table.append("-+-".join("-" * width for width in column_widths))  # Разделитель

    for row in data[1:]:
        table.append(format_row(row))  # Данные

    return "\n".join(table)
