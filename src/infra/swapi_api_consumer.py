from typing import Dict, Tuple, Type
from collections import namedtuple
import requests
from requests import Request
from src.errors import HttpRequestError

class SwapiApiConsumer:
    '''
        Class to consume swapi api with http requests.
    '''

    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code request response')

    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''
            request starships in pagination.
            :param page: pagination page
            :return: status_code, request, response
        '''
        request = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships',
            params={"page": page}
            )

        request_prepare = request.prepare()
        response = self.__send_http_request(request_prepare)
        status_code = response.status_code

        if status_code >= 200 and status_code < 300:
            return self.get_starships_response(
                status_code=status_code,
                request=request,
                response=response.json()
            )
        else:
            raise HttpRequestError(
                    status_code=status_code,
                    message=response.json()['detail']
                )


    @classmethod
    def __send_http_request(cls, request: Type[Request]) -> any:
        '''
            Prepare a session and send http request.
            :param request: Request object.
            :return: http Response object.
        '''
        response = requests.Session().send(request)
        return response
