import pytest

from furrycorn import config
from furrycorn.model import errors


def test_mk_single(mocker):
    obj = {} # mock
    cfg = config.mk('https://api', 'ABCDEF')

    result = errors.mk_single(obj, cfg)

    assert type(result) is errors.Error


def test_mk(mocker):
    obj = [ {}, {}, {} ] # mock
    cfg = config.mk('https://api', 'ABCDEF')

    result = errors.mk(obj, cfg)

    assert type(result) is errors.Errors

