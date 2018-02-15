from stream import Book




book = 'C:/Users/Jaime Velez/Documents/GitHub/pynot/literature_moby.txt'
nochapters = True
stats = True
bookObj = Book(book, nochapters, stats)
stat=bookObj.getHeadings()
print(bookObj.chapters[137])
dorec = bookObj.getTextBetweenHeadings()
print(dorec)

