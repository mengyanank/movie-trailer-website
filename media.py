import webbrowser

class Movie:
    def __init__(self, title, image_url, trailer_url):
        # movie's title
        self.title = title
        # movie's image location
        self.poster_image_url = image_url
        # movie's trailer url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self): # open the url in browser
        webbrowser.open(self.trailer_youtube_url)
