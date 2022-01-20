import xml.etree.ElementTree as ET
from collections import Counter

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
descriptions = root.findall("channel/item")
array = list()
for description in descriptions:
    words = description.find("description").text.split(" ")
    for word in words:
        if len(word) >= 6:
            array.append(word)
print("ТОП 10 самых встречаемых слов:")
num_str = 0
for print_word, count in Counter(array).most_common()[0:10]:
    num_str += 1
    print(f'{num_str}. Слово "{print_word}" встречается в файле {count} раз(а)')