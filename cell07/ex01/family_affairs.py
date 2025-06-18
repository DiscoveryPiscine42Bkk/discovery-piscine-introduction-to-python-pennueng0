def genopum(family):
    return list(filter(lambda name: family[name]== "pupennueng", family.keys()))

dupont_family = {
    "pennueng": "pennueng",
    "geno": "geno",
    "mairu": "tem",
    "chutinun": "pupennueng",
    "yungmak": "pupennueng"
}

print(genopum(dupont_family))