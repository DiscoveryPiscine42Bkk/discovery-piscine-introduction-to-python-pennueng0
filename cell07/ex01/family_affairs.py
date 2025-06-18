def jenopennueng(family):
    return list(filter(lambda name: family[name] == "pennueng", family.keys()))

dupont_family = {
    "pennueng": "pennueng",
    "่jeno": "jeno",
    "mairu": "tem",
    "moruedi": "pennueng",
    "yachai": "pennueng"
}

print(jenopennueng(dupont_family))