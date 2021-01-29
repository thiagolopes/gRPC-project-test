from decimal import Decimal

from apps.commons.utils import ftod


def test_tfod():
    assert ftod(13.12) == Decimal("13.12")
