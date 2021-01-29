import functools
import logging

import grpc
from django.conf import settings
from google.protobuf.json_format import MessageToDict

logger = logging.getLogger(__name__)


def proto2dict(f):
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        return MessageToDict(f(*args, **kwargs))
    return wrap


class BaseStub:
    stub_class = None

    def __init__(self, channel=None):
        if not channel:
            logger.info("insecure_channel_used, %s", type(self))
            channel = grpc.insecure_channel(settings.INSECURE_GRPC_HOST)

        self.channel = channel
        self.client = self.stub_class(self.channel)
