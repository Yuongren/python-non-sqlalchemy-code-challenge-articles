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

    all_magazines = []  # Store all magazines globally

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")

        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    def __str__(self):
         # Returns a formatted string showing the magazine's name and category.
        return f"{self.name} ({self.category})"  
    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return None if not titles else titles

    def contributing_authors(self):
        author_counts = {author: 0 for author in self.contributors()}
        for article in self.articles():
            author_counts[article.author] += 1
        result = [author for author, count in author_counts.items() if count > 2]
        return None if not result else result

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_counts = {magazine: 0 for magazine in cls.all_magazines}
        for article in Article.all:
            magazine_counts[article.magazine] += 1
        return max(magazine_counts, key=magazine_counts.get)
    
