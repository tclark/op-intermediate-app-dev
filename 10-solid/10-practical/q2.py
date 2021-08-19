class BlogPost:
    """Adds a post to the blog and provides a save() method for it."""
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self._db = Database()
        
    def save(self):
        try:
            self._db.save(self)
        except DBAPIError as e:
            with open(ERRLOG, 'a') as log:
                log.write('Error saving blog post:')
                log.write(e)
