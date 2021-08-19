class BlogPost:
    """This looks like the BlogPost from an earlier question, but there is an important difference."""
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self._db = Database()
        self.error_log = FileLogger(ERRLOG)
        
    def save(self):
        try:
            self._db.save(self)
        except DBAPIError as e:
            self.error_log.write('Error saving blog post:')
            self.error_log.write(e)