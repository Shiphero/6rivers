from .common import SixRiverSchema


class Deserializer:

    """
    Keeps track of registered schemas and deserializes message payloads
    """

    @classmethod
    def deserialize(cls, data: dict):
        """
        Deserialize a payload, building the corresponding schema

        Parameters:
          - data: A message payload

        Returns:
          An deserialized entity
        """
        for s in SixRiverSchema.__subclasses__():
            if s.__schema_name__ and data.get('messageType') == s.__schema_name__:
                return s().load(data)
        else:
            raise ValueError("Unknown message type")
