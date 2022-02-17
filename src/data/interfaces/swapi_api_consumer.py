from abc import ABC, abstractmethod
from typing import Dict, Tuple, Type
from requests import Request

class SwapiApiConsumerInterface(ABC):
    '''
    Interface for SwapiApiConsumer
    '''

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''
        Must implement
        '''
        raise Exception('Must implement get_starships method')
