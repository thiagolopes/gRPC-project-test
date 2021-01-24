from unittest.mock import Mock

from apps.commons.stubs import BaseStub


# test logging
def test_base_stub():
    stub_mock = Mock()
    channel_mock = Mock()
    BaseStub.stub_class = stub_mock

    base_stub = BaseStub(channel=channel_mock)

    assert base_stub.channel is channel_mock
    stub_mock.assert_called_with(channel_mock)
