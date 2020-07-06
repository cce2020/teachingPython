# Optimized for 30 bible books

books = ["genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "samuel", "kings", "chronicles", "ezra", "nehemiah",
        "esther", "job", "psalms", "proverbs", "ecclesiastes", "song of songs", "isaiah", "jeremiah", "lamentations", "ezekiel", "daniel", "hosea",
        "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "haggai", "zechariah", "malachi", "matthew", "mark", "luke",
        "john", "acts", "romans", "corinthians", "galatians", "ephesians", "philippians", "colossians", "thessalonians", "timothy", "titus", "philemon",
        "hebrews", "james", "peter", "jude", "revelation"]

contains = []

def main():
    # Initialization of text
    text = open("text.txt", "r")    # Creates a file object (text) that the program can read ("r")
    contents = text.read()          # Saves all text on the file as a single string (contents)

    # Removes any puncuation, line breaks, and spaces
    contents = contents.replace(' ', '')
    contents = contents.replace('\n', '')
    contents = contents.replace('.', '')
    contents = contents.replace(',', '')
    contents = contents.replace('?', '')
    contents = contents.replace('\'', '')
    contents = contents.replace('\"', '')

    # Makes all of the letters lowercase since lowercase letters
    # are different from uppercase letters which will cause missed results
    contents = contents.lower()

    # Actual searching of the text
    for title in books:
        if title in contents:
            contains.append(title.capitalize())
    print(contains)
    print(len(contains))

main()
