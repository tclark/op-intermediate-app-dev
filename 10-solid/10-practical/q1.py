

class PostComment:
    """PostComment can be used to represent a comment or a tag added to a blog post."""
    def __init__(self, blogpost, message):
        if message[0] == '#':
            # it's a tag
            blogpost.add_tag(message)
        else:
            blogpost.add_comment(message)