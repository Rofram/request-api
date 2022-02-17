from abc import ABC, abstractmethod
from typing import List, Dict

class StarshipsListCollectorInterface(ABC):
    '''
        Interface for StarshipsListCollector
    '''

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        '''
            Returns a list of starships
        '''
        raise Exception('Must implement list method')
