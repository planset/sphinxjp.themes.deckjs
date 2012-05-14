# -*- coding: utf-8 -*-
"""
    sphinxjp.themes.deckjs.directives
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Deckjs.js Style specific HTML tag builder.

    :copyright: Copyright (c) 2012, by Sphinx-users.jp, See AUTHORS.
    :license: MIT, see LICENSE for details.
"""

from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes
from docutils import nodes
from sphinx.util.compat import Directive

__docformat__ = 'reStrructuredText'

theme_style = None
theme_transition = None


class deckjs_title(nodes.General, nodes.Element): pass
class DeckjsTitle(Directive):
    """
    A impressjs entry, control impressjs slide effects, actions and styles.
    """
    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True
    node_class = deckjs_title

    def run(self):
        node = deckjs_title(title=self.arguments[0])
        return [node]

def visit_deckjs_title(self, node):
    title = node['title']
    self.body.append(self.starttag(node, 'h2'))
    self.body.append(title)

def depart_deckjs_title(self, node=None):
    self.body.append('</h2>\n')

    

class deckjs(nodes.General, nodes.Element): pass


class Deckjs(Directive):
    """
    A impressjs entry, control impressjs slide effects, actions and styles.
    """
    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True

    option_spec = {
        'data-x': int,
        'data-y': int,
        'data-z': int,
        'data-rotate-x': int,
        'data-rotate-y': int,
        'data-rotate': int,
        'data-scale-x': int,
        'data-scale-y': int,
        'data-scale': int,
        'class': directives.class_option ,
    }

    node_class = deckjs

    def run(self):
        """ build deckjs node """
        set_classes(self.options)
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = self.node_class(text, **self.options)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        if self.arguments[0]:
            node['ids'] += [self.arguments[0]]
        if 'class' in self.options:
            node['classes'].append(options['class'])

        return [node]


def visit_deckjs(self, node):
    """ build div start tag for deck.js """
    atts = {'class': 'slide'}
        
    if 'data-x' in node:
        atts['data-x'] = node['data-x']
    if 'data-y' in node:
        atts['data-y'] = node['data-y']
    if 'data-z' in node:
        atts['data-z'] = node['data-z']
    if 'data-rotate-x' in node:
        atts['data-rotate-x'] = node['data-rotate-x']
    if 'data-rotate-y' in node:
        atts['data-rotate-y'] = node['data-rotate-y']
    if 'data-rotate' in node:
        atts['data-rotate'] = node['data-rotate']
    if 'data-scale-x' in node:
        atts['data-scale-x'] = node['data-scale-x']
    if 'data-scale-y' in node:
        atts['data-scale-y'] = node['data-scale-y']
    if 'data-scale' in node:
        atts['data-scale'] = node['data-scale']

    self.body.append(self.starttag(node, 'section', **atts))
    self.set_first_last(node)


def depart_deckjs(self, node=None):
    """ build div end tag """
    self.body.append('</section>\n')


def setup(app, **kwargs):
    global theme_style, theme_transition
    app.add_node(deckjs,
                 html=(visit_deckjs, depart_deckjs))
    app.add_directive('deckjs', Deckjs)
    app.add_node(deckjs_title,
                 html=(visit_deckjs_title, depart_deckjs_title))
    app.add_directive('deckjs_title', DeckjsTitle)
