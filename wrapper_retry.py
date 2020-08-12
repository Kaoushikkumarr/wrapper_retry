import requests
from retry import retry
from abc import ABC, abstractmethod
from config.config import PLATFORM_URL, PATH_FINDER


class Wrap_api_url(ABC):

    @abstractmethod
    def method_call(self, method, url, **kwargs):
        pass

    @abstractmethod
    def create_url(self,  *args, **kwargs):
        pass


class Wrap_url_create(Wrap_api_url):

    @retry(exceptions=Exception, tries=3, delay=0, max_delay=None)
    def method_call(self, method, url, **kwargs):
        result = requests.request(method, url, **kwargs)
        return result

    def create_url(self, *args, **kwargs):
        base_url = PLATFORM_URL + '/' + PATH_FINDER  # import STATIC variables from config.config
        url = '/'.join([base_url, *args])
        return url
