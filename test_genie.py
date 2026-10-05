import pytest

from genie import Gift

def test_gift_creation():
    gift = Gift(
        name="Hiking Backpack",
        reason="Perfect for someone who loves hiking.",
        price="$75"
    )

    assert gift.name == "Hiking Backpack"
    assert gift.reason == "Perfect for someone who loves hiking."
    assert gift.price == "$75"

def test_gift_requires_name():
    with pytest.raises(Exception):
        Gift(
            reason="Perfect for someone who loves hiking.",
            price="$75"
        )