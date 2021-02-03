from datetime import datetime


def get_release_date(release_str):
    date_str = release_str.replace("Day of release: ", "")
    return datetime.strptime(date_str, "%d %B %Y")
