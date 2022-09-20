from pickle import TRUE
from datetime import date

AUTHOR = 'Tiffanie'
SITENAME = 'Koala Kiwi'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/tiffanie_boreux'),
    ('github', 'https://github.com/tt-bb'),
    ('instagram', 'https://www.instagram.com/tiffanie.boreux/')
)

# THEME
MAIN_MENU = TRUE
CATEGORIES_SAVE_AS = 'category/{slug}.html' 
ARCHIVES_SAVE_AS = 'archives.html'
MENUITEMS = (
    ('Categories', '/' + CATEGORIES_SAVE_AS),
    ('Archives', '/' + ARCHIVES_SAVE_AS),
    ('Tags', '/tags.html')
)

DEFAULT_PAGINATION = 20
THEME = "flex"
BROWSER_COLOR = '#4CAF50'
COPYRIGHT_YEAR = date.today().year
COPYRIGHT_NAME = 'tt-bb'
SITELOGO = 'https://www.gravatar.com/avatar/6252ddf78109f0b06bcc8cd962287c5d?size=400'
FAVICON = SITEURL + '/images/favicon.ico'