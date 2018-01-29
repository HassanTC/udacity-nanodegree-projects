class Movie():
    """
        A movie class where u can create new instance of movie with
        (title, poster_image_url and trailer_youtube_url)
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ create new movie instance by title, image_url, trailer_url """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
