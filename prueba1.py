from stream import Book




book = 'literature_moby.txt'
nochapters = False
stats = True
bookObj = Book(book, nochapters, stats)
stat=bookObj.getHeadings()
print(bookObj.chapters[137])


