import pytest

from genie import Gift, GiftList, find_gifts


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


class FakeResponse:
    def __init__(self):
        self.output_parsed = GiftList(
            gifts=[
                Gift(
                    name="Test Gift",
                    reason="A test reason",
                    price="$25"
                )
            ]
        )


class FakeResponses:
    def parse(self, **kwargs):
        return FakeResponse()


class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()


def test_find_gifts():
    client = FakeClient()

    result = find_gifts(
        "my brother",
        "$50",
        "Birthday",
        client
    )

    assert isinstance(result, GiftList)
    assert len(result.gifts) == 1
    assert result.gifts[0].name == "Test Gift"
    assert result.gifts[0].price == "$25"