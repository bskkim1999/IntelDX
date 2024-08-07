class Book:
    def __init__(self, title, isbn):
        self.__title=title
        self.__isbn=isbn
        
    def __repr__(self):
        return "ISBN :"+self.__isbn+", Name : "+self.__title
    
book = Book("the python tutorial", "21321321")
book2 = Book("the machine language", "54564546")

print(book)
print(book2)