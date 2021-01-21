import logging

import grpc

logger = logging.getLogger(__name__)


class BaseStub:
    stub_class = None

    def __init__(self, channel=None):
        if not channel:
            logger.info("insecure_channel_used, %s", type(self))
            channel = grpc.insecure_channel("localhost:50051")

        self.channel = channel
        self.client = self.stub_class(self.channel)
