# Importing native packages:
import time

# Importing thrid party packages:
import requests
from bs4 import BeautifulSoup
import datetime

class BaseWebPageResponse(object):
    """
    A Class representing a webpage extracted via requests libary.

    This is the Base class for all webpage objects used by web scrapers in the
    library. It contains all the HTML contents of the webpage extracted via the
    requests libary as well as relevant metadata about said contents extraction:
    date, etc.... Practically this base object is meant to serve as a rough
    abstraction layer for the result of the requests.get() method. It facilitates
    the creation of custom web page objects to be used by each web scraper in the
    library.

    Attributes:

        _name (str): The string that is used to identify the web object. This string
            is used to identify the tablename associated with writing the WebObject
            to a database via the __repr__ method.

        _url (str): The url of the webpage to be accessed with requests.get

        _initialized_time (float): The python timestamp when the object was
            initialized. It is created at the instance the WebObject is initialized
            via datetime.datetime.now()

        _kwargs (dictionary): Optional arguments that modify functionality of
            various methods within the object as well future-proofing further
            development of the Base Class.

        _http_response (requests.Response): The HTTP Response generated by the
            webpage to which a GET request was sent. This is the result from the
            requests.get object.

        _html_body (BeautifulSoup obj): The root BeautifulSoup object that contains
            all the nested HTML objects returned by the HTTP GET request. This
            contains all of the HTML content of the webpage.

    """

    def __init__(self, url, **kwargs):

        # Declaring all _private instance variables:
        self._kwargs = kwargs
        self._url = url
        self._initialized_time = datetime.datetime.now()

        # HTTP requests.Response object.
        self._http_response = self.__perform_get_request()

        # BeautifulSoup object for HTML body of response:
        self._html_body = self._http_response.content

    def __perform_get_request(self):
        '''
        Internal method that performs the request.get() HTTP requests.

        The internal method performs the HTTP GET request to the url specificed
        by the self._url instance variable. It uses the requests.get() method to
        perform said GET request. In addition to the url it also passes in the
        'params' argument of the main objects **kwargs if present.

        Returns:
            response_obj: The result of the request.get() method- A requests.Response
                object.

        '''
        # Determining if the 'params' key-word argument has been passed:
        if 'params' in self._kwargs:

            # Try-Catch for the 'params' kwarg mainly to assert dictionary type:
            try:

                respone_obj = requests.get(self._url, params=self.kwargs['params'])
                return respone_obj

            except (AttributeError, TypeError):
                raise AssertionError("kwargs['params'] must be type dictionary")

        else:

            respone_obj = requests.get(self._url)
            return respone_obj

    def __repr__(self):
        return f'WebObject({self._url}_{self._initialized_time})'
