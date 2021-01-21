# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import apps.stubs.promotion_pb2 as promotion__pb2


class DiscountServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AvailableDiscounts = channel.unary_unary(
            "/discount.DiscountService/AvailableDiscounts",
            request_serializer=promotion__pb2.Order.SerializeToString,
            response_deserializer=promotion__pb2.Discounts.FromString,
        )


class DiscountServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AvailableDiscounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DiscountServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AvailableDiscounts": grpc.unary_unary_rpc_method_handler(
            servicer.AvailableDiscounts,
            request_deserializer=promotion__pb2.Order.FromString,
            response_serializer=promotion__pb2.Discounts.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler("discount.DiscountService", rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DiscountService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AvailableDiscounts(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/discount.DiscountService/AvailableDiscounts",
            promotion__pb2.Order.SerializeToString,
            promotion__pb2.Discounts.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
