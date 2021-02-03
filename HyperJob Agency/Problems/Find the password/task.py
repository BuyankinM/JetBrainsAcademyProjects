from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    password = get_pass_from_elem(root)
    return password


def get_pass_from_elem(parent):
    password = None

    if "password" in parent.keys():
        return parent.get("password")

    for child in parent:
        password = get_pass_from_elem(child)
        if password:
            break

    return password
