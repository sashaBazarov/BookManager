def generate_table(data: list, headers: list = None):
    if not data:
        return "No data available."

    if headers:
        data = [headers] + data

    column_widths = [
        max(len(str(row[i])) for row in data) for i in range(len(data[0]))
    ]

    def format_row(row):
        return " | ".join(str(cell).ljust(width) for cell, width in zip(row, column_widths))

    table = []
    table.append(format_row(data[0])) 
    table.append("-+-".join("-" * width for width in column_widths))

    for row in data[1:]:
        table.append(format_row(row)) 
    
    return "\n".join(table)
