def open_text(filename):
    with open(filename, 'r', encoding='utf8') as rf:
        return rf.read()