from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships(requests_mock):
    '''
        Test the get_starships method of the SwapiApiConsumer class.
    '''

    # Mock the response from the API
    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'results': [{'name': 'Starship 1'}, {'name': 'Starship 2'}]})
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
