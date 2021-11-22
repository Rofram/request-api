from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships():
    '''
        Test the get_starships method of the SwapiApiConsumer class.
    '''
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
