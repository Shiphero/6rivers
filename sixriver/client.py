import logging
import requests
import inspect

from urllib.parse import urljoin
from functools import reduce

from . import messages


logger = logging.getLogger(__name__)


def slash_join(*args):
    return reduce(urljoin, args).rstrip("/")


class SixRiverClientError(Exception):

    def __init__(self, url, response):
        self.url = url
        self.status_code = response.status_code
        self.error_code = None

        try:
            data = response.json()
            message = data.get('message', None)

            self.error_code = data.get('statusCode', None)

        except ValueError:
            message = response.text

        super(SixRiverClientError, self).__init__(message)


class SixRiverClient:

    """
    An http json client that post messages to the six river server

    """

    def __init__(self,
        token: str,
        url: str ="https://sixdk.6river.tech/",
        env: str ="prod",
        version: str ="v2"
    ):
        self._token = token
        self._headers = {
            "Content-Type": "application/json",
            "6DK-Token": token
        }
        self._url = f"{url}/{env}/{version}"

    def send(self, msg: messages.SouthboundMessage):
        """
        Given a six river message that correlates with one of the
        supported endpoints, we serialize it and post to the six river
        url

        Parameters:
        - msg: A SouthboundMessage that corresponds to a supported endpoint


        Returns:
          The result of the post call to the message endpoint
        """
        endpoint = getattr(msg, '__endpoint__', None)
        method = getattr(msg, '__http_method__', None)

        if inspect.ismethod(method):
            method = method.__func__

        if not endpoint:
            raise TypeError(
                f"Unsupported message of type {type(msg)}. " \
                f"Expected instance of {messages.SouthboundMessage.__name__}"
            )

        url = slash_join(self._url, endpoint)

        logger.info("Calling 6river [{}] {}".format(method, url))

        res = method(url, json=msg.serialize(), headers=self._headers)

        if res.status_code >= 300:
            raise SixRiverClientError(url, res)

        return res.json()

