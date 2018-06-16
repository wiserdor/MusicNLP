class Song:
    def __init__(self, name, length, genre=None, sentiment=None, date_published=None, date_created=None,
                 corpuses_used=[]):
        self.name = name
        self.length = length
        self.genre = genre
        self.sentiment = sentiment
        self.date_published = date_published
        self.date_created = date_created
        self.corpuses_used = corpuses_used
        self.template_num
