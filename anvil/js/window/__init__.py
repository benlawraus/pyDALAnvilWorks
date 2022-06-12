from unittest.mock import Mock
from dataclasses import dataclass, field


def Function(*args, **kwargs):
    return Mock()


Promise = Mock()

document = Mock()
document.body = Mock()

jQuery = Mock()
jQuery.appendTo = Mock()


def addEventListener(*args, **kwargs):
    return Mock()


def removeEventListener(*args, **kwargs):
    return Mock()
