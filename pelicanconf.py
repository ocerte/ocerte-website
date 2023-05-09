AUTHOR = 'Peter D. Kazarinoff'
SITENAME = 'OCERTE Website'
SITEURL = ''

# Path Seetings
PATH = 'content'
PAGE_PATHS = [
    'pages'
]

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Theme
THEME = "./simplify-theme"
THEME_TEMPLATES_OVERRIDES = ['theme-overrides']

# Pages: like the about page
DISPLAY_PAGES_ON_MENU = True

# URLs
REALTIVE_URLS = True

# Site Map from the sitemap Pelican plugin
SITEMAP = {
    'format':'xml'
    }
