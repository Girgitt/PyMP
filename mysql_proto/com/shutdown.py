# coding=utf-8

from ..packet import Packet
from ..proto import Proto
from ..flags import Flags


class Shutdown(Packet):
    __slots__ = ('shutdownType')

    def __init__(self):
        super(Shutdown, self).__init__()
        self.shutdownType = Flags.SHUTDOWN_DEFAULT

    def getPayload(self):
        payload = bytearray()

        payload.extend(Proto.build_byte(Flags.COM_SHUTDOWN))
        if self.shutdownType != Flags.SHUTDOWN_DEFAULT:
            payload.extend(Proto.build_fixed_int(1, self.shutdownType))

        return payload

    @staticmethod
    def loadFromPacket(packet):
        obj = Shutdown()
        proto = Proto(packet, 3)

        obj.sequenceId = proto.get_fixed_int(1)
        proto.get_filler(1)
        obj.shutdownType = proto.get_fixed_int(1)

        return obj
