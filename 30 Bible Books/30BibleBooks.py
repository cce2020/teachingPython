# Optimized for 30 bible books

books = ["genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "samuel", "kings", "chronicles", "ezra", "nehemiah",
        "esther", "job", "psalms", "proverbs", "ecclesiastes", "song of songs", "isaiah", "jeremiah", "lamentations", "ezekiel", "daniel", "hosea",
        "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke",
        "john", "acts", "romans", "corinthians", "galatians", "ephesians", "philippians", "colossians", "thessalonians", "timothy", "titus", "philemon",
        "hebrews", "james", "peter", "jude", "revelation"]

contains = []

def main():
    text = open("text.txt", "r")    # Read only mode
    contents = text.read()
    contents = contents.replace(' ', '')
    contents = contents.replace('\n', '')
    contents = contents.replace('.','')
    contents = contents.replace(',','')
    contents = contents.replace('?','')
    contents = contents.replace('\'','')
    contents = contents.replace('\"','')
    contents = contents.lower()
    for title in books:
        if title in contents:
            contains.append(title.capitalize())
    print(contains)
    print(len(contains))

main()
