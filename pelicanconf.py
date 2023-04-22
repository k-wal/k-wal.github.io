AUTHOR = 'k-wal'
SITENAME = "k-wal's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# by me: adding output file for github
OUTPUT_PATH = 'docs/'

# Path to the folder containing the plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican-ipynb.markup']
MARKUP = ('md', 'ipynb')
IPYNB_USE_METACELL = True

IGNORE_FILES = [".ipynb_checkpoints"]

#THEME = 'attila-1.6'

# THEME = 'themes/pelican-alchemy/alchemy'
# THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']

THEME = 'Flex'
PYGMENTS_STYLE = "default"
THEME_COLOR = "light"