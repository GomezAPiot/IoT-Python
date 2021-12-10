import urllib2
from model import *
from format import *
from exception import *

# curl 'api.irail.be/liveboard/?station=gentbruggee&format=json'

BASE_URL = "http://api.irail.be/"
URLS = {
    'stations': 'stations',
    'schedules': 'connections',
    'liveboard': 'liveboard',
    'vehicle': 'vehicle'
}
DEFAULT_ARGS = "?format=json"


class iRailAPI:

    def __init__(self, format=None, lang=None):
        self.set_format(format)
        self.set_lang(lang)

    def format(self):
        return self.__format

    def set_format(self, format):
        if format:
            self.__format = format
        else:
            self.__format = JsonFormat()

    def lang(self):
        return self.__lang

    def set_lang(self, lang):
        if lang:
            self.__lang = lang
        else:
            self.__lang = "EN"

    def do_request(self, method, args=None):
        url = BASE_URL + method + "/"
        url += "?format=" + str(self.format())
        url += "&lang=" + self.lang()
        if args:
            for key in args.keys():
                url += "&" + key + "=" + args[key]
        try:
            return urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            if e.code >= 400 and e.code < 500:
                raise ClientError(e)
            elif e.code >= 500 and e.code < 500:
                raise ServerError(e)
