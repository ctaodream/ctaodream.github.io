#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ctaodream'
SITENAME = u'NSLOG CLUB !'
#SITEURL = 'http://nslog.club'
SITESUBTITLE = 'Coding every day == smile every day !'

MENUITEMS = (
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
    ('Archives', '/functions/archives.html'),
)

PATH = 'content'

GOOGLE_ANALYTICS = 'UA-70082794-1'
GOOGLE_ANALYTICS_SITENAME = 'www.nslog.club'

FACEBOOK_URL = 'https://www.facebook.com/yang.xu.96558061'
GOOGLEPLUS_URL = 'https://plus.google.com/u/0/117263032165097338865'
TWITTER_URL = 'https://twitter.com/xuyangfighting'
GITHUB_URL = 'https://github.com/ctaodream'
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

THEME = 'pelican-themes/gum'
DISQUS_SITENAME = 'nslogclub'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


#CATEGORIES_URL = u'/categories.html'
#CATEGORIES_SAVE_AS = u'/categories.html'

#TAGS_URL = '/tags.html'
#TAGS_SAVE_AS = '/tags.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# Social widget
SOCIAL = (('Github', 'https://github.com/ctaodream'),
          ('Quora', 'http://www.quora.com/Zherui-Li'),
          ('Twitter', 'https://twitter.com/lzrak47'),
          ('Facebook', 'https://www.facebook.com/profile.php?id=100004875786021'),
          ('Linkedin', 'http://www.linkedin.com/profile/view?id=232391796'),
          (u'微博', 'http://weibo.com/lzrm4a1'),
          (u'知乎', 'http://www.zhihu.com/people/li-zhe-rui'),
          (u'豆瓣', 'http://www.douban.com/people/lizherui'),
         )


DEFAULT_PAGINATION = 5

# plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap','summary']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
