# coding=utf-8

from ..packet import Packet
from ..proto import Proto
from ..flags import Flags


class Setoption(Packet):
    __slots__ = ('operation', ) + Packet.__slots__

    def __init__(self):
        super(Setoption, self).__init__()
        self.operation = 0

    def getPayload(self):
        payload = bytearray()

        payload.extend(Proto.build_byte(Flags.COM_SET_OPTION))
        payload.extend(Proto.build_fixed_int(2, self.operation))

        return payload

    @staticmethod
    def loadFromPacket(packet):
        obj = Setoption()
        proto = Proto(packet, 3)

        obj.sequenceId = proto.get_fixed_int(1)
        proto.get_filler(1)
        obj.operation = proto.get_fixed_int(2)

        return obj
