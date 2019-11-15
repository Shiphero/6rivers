

class Deserializer:

    """
    Keeps track of registered schemas and deserializes message payloads
    """

    _schemas = []

    @classmethod
    def deserialize(
      cls,
      data,  # dict
    ):
        """
        Deserialize a payload, building the corresponding schema

        Parameters:
          - data: A message payload

        Returns:
          An deserialized entity
        """
        for s in cls._schemas:
            if s.__schema_name__ and data.get('messageType') == s.__schema_name__:
                return s().load(data)
        else:
            raise ValueError("Unknown message type")


def register_schema(klas):
    if klas not in Deserializer._schemas:
        Deserializer._schemas.append(klas)

    return klas
