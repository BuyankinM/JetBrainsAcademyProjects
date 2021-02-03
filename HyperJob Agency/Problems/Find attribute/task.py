from lxml import etree

root = etree.fromstring(input())
key = input()

if key in root.keys():
    print(root.get(key))
else:
    print(None)