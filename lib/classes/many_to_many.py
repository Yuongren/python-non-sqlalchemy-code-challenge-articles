class Article:
    
    all = []  # Store all articles globally

    def __init__(self, author:str, magazine:str, title:str):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # Register the article globally
    
    def __str__(self):
         # Returns a formatted string showing the article's title and its author.
        return f"'{self.title}' by {self.author}" 

class Author:
    def __init__(self, name:str):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name

    def __str__(self):
        # Returns the author's name when the object is printed or converted to a string.
        return self._name   # Return a readable string for the author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable and cannot be changed.")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):

        magazines = self.magazines()
        return None if not magazines else list(set(magazine.category for magazine in magazines))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass