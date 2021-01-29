from unittest.mock import Mock, patch

from apps.commons.stubs import BaseStub, proto2dict
from apps.stubs.promotion_pb2 import Discount


def test_base_stub(caplog):
    stub_mock = Mock()
    channel_mock = Mock()
    BaseStub.stub_class = stub_mock

    base_stub = BaseStub(channel=channel_mock)

    assert base_stub.channel is channel_mock
    stub_mock.assert_called_with(channel_mock)
    assert caplog.text == ""


@patch("grpc.insecure_channel")
def test_base_stub(grpc_mock, caplog, settings):
    stub_mock = Mock()
    BaseStub.stub_class = stub_mock

    base_stub = BaseStub()

    assert caplog.text == ""
    grpc_mock.assert_called_with(settings.INSECURE_GRPC_HOST)


def test_proto2dict():
    @proto2dict
    def example_test():
        d = Discount()
        d.percentage = 0.1
        d.discount_name = "test_discount"
        return d

    assert example_test() == {"percentage": 0.1, "discountName": "test_discount"}
