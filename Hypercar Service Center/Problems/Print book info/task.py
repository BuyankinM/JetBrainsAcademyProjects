def print_book_info(title, author=None, year=None):
    mas_str = [f'"{title}"']
    if author is not None or year is not None:
        mas_str.append("was written")

        if author is not None:
            mas_str.append(f"by {author}")

        if year is not None:
            mas_str.append(f"in {year}")

    print(" ".join(mas_str))