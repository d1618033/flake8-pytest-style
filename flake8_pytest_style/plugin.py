import argparse
from typing import List

from flake8.options.manager import OptionManager
from flake8_plugin_utils import Plugin

from .config import Config
from .visitors import PytestStyleVisitor

__version__ = '0.2.0'


class PytestStylePlugin(Plugin[Config]):
    name = 'flake8-pytest-style'
    version = __version__
    visitors = [PytestStyleVisitor]

    @classmethod
    def add_options(cls, option_manager: OptionManager) -> None:  # pragma: no cover
        option_manager.add_option(
            '--no-bare-raises-exceptions', comma_separated_list=True
        )

    @classmethod
    def parse_options_to_config(  # pylint: disable=unused-argument
        cls, option_manager: OptionManager, options: argparse.Namespace, args: List[str]
    ) -> Config:  # pragma: no cover
        return Config(no_bare_raises_exceptions=options.no_bare_raises_exceptions)
