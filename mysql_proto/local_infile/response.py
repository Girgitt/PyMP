#!/usr/bin/env python
# coding=utf-8

from packet import Packet
from proto import Proto


class Response(Packet):
    __slots__ = ('data',) + Packet.__slots__

    def __init__(self):
        super(Response, self).__init__()
        self.data = bytearray()

    def getPayload(self):
        return self.data

    @staticmethod
    def loadFromPacket(packet):
        obj = Response()
        proto = Proto(packet, 3)

        obj.sequenceId = proto.get_fixed_int(1)
        obj.data = proto.packet[proto.offset:]

        return obj

if __name__ == "__main__":
    import doctest
    doctest.testmod()
