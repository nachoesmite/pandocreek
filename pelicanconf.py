AUTHOR = 'nacho esmite'
SITENAME = 'pandocreek'
SITEURL = ""
STATIC_PATHS = ['draws', 'images']
PATH = "content"
# Save path for author pages
AUTHOR_SAVE_AS = 'author/{slug}.html'
# URL for author pages
AUTHOR_URL = 'author/{slug}.html'
TIMEZONE = 'America/Montevideo'
MENUITEMS = (
    ('Home', '/'),
)
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
# Blogroll
LINKS = (
    ("Bluesky", "https://bsky.app/profile/pandocreek.com"),
    ("Github", "https://github.com/nachoesmite"),
    ("Linkedin", "https://www.linkedin.com/in/iesmite/"),
)

# Social widget
#SOCIAL = (
#    ("Bluesky", "https://bsky.app/profile/pandocreek.com"),
#    ("Github", "https://github.com/nachoesmite"),
#    ("Linkedin", "https://www.linkedin.com/in/iesmite/"),
#)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
