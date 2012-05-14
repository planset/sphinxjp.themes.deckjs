===========================
 sphinxjp.themes.deckjs
===========================

Impress.js presentation style theme for Sphinx.


Output sample
=============
:output: http://packages.python.org/sphinxjp.themes.deckjs
:source: http://packages.python.org/sphinxjp.themes.deckjs/_sources/index.txt


Feature
=======
* provide ``deckjs`` directive for impress.js presentaion control
* provide ``deckjs`` presentation theme for render HTML document


Installation
============
Make environment with easy_install::

   $ easy_install sphinxjp.themes.deckjs


setup conf.py with::

   extensions = ['sphinxjp.themecore']
   html_theme = 'deckjs'
   html_use_index = False


and run::

   $ make html


Requirement
===========
Libraries:

* Python 2.4 or later (not support 3.x)
* Sphinx 1.0.x or later.


Browsers:

* Safari
* Chrome
* Firefox 10


License
=======
Licensed under the `MIT license <http://www.opensource.org/licenses/mit-license.php>`_ .
See the LICENSE file for specific terms.


.. END
