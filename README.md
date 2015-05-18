### iegget
Django project for iegget.no

django-wiki-based "blog" where the front page pulls the latest articles from the wiki and represents them in a similar fashion as one would on a blog.
Every template extends from the wiki base to provide a similar look and feel to all pages.

The icons for the mime types are from [MimeTypes-Link-Icons](https://github.com/eagerterrier/MimeTypes-Link-Icons)

TODO:
- change to ldap auth backend
- make some sort of SSO solution to be used across different webapps
- find some way to remove the "Sign up" link on all wiki pages


#### *nix requirements

For images in django-wiki

    apt-get install libjpeg-dev zlib1g-dev libpng12-dev 

Reinstall pillow afterwards to compile with support for the formats above

    pip uninstall pillow
    pip install pillow
