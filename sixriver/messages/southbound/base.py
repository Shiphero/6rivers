

class SouthboundMessage:

    __endpoint__ = None
    __http_method__ = None

    def serialize(self):
        raise NotImplementedError

