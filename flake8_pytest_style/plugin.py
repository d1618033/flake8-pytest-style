from flake8_plugin_utils import Plugin

from .visitors import PytestStyleVisitor

__version__ = '0.1.3'


class PytestStylePlugin(Plugin):
    name = 'flake8-return'
    version = __version__
    visitors = [PytestStyleVisitor]
