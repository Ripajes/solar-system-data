import requests
from pandas import json_normalize
from os import path

class MyException(Exception):
    def __init__(self, message):
        self.message = message

def get_solar_systems_bodies(params:dict=None)->object:
    """A function that requests Solar System REST API for more information see: https://api.le-systeme-solaire.net/

    Args:
        params (dict, optional): parameters of request, see documentation. Defaults to None.

    Raises:
        MyException: _description_

    Returns:
        object: json object with bodies data
    """
    api_url = 'https://api.le-systeme-solaire.net/rest/bodies/'
    if params:
        response = requests.get(api_url, params=params)
    else:
        response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise MyException('Bad request status code: {0}'.format(response.status_code))

def get_planets()->object:
    """A function to get planets data from Solar System REST API.

    Returns:
        object: pandas dataframe with name, mass, vol, gracity and dicoveryDate values
    """
    params = {
        'data': 'englishName,massValue,,mass,massExponent,vol,volValue,volExponent,gravity,discoveryDate',
        'filter[]': 'isPlanet,neq,False',
        'order': 'volExponent,desc,volValue,desc'
    }
    planets = get_solar_systems_bodies(params=params)['bodies']
    df_planets = json_normalize(planets, sep='_',)
    df_planets['vol'] = df_planets['vol_volValue'].astype(str) + "e" + df_planets["vol_volExponent"].astype(str)
    df_planets['vol'] = df_planets['vol'].astype(float)
    df_planets['mass'] = df_planets['mass_massValue'].astype(str) + "e" + df_planets["mass_massExponent"].astype(str)
    df_planets['mass'] = df_planets['mass'].astype(float)
    df_planets.drop(columns=['vol_volValue', 'vol_volExponent', 'mass_massValue', 'mass_massExponent', ], inplace=True)
    return df_planets


def main():
    planets = get_planets()
    save_file = path.join(path.dirname(__file__), 'data', 'planets.json')
    planets.to_json(path_or_buf=save_file,index=True, orient='records')
    print('finished')

if __name__ == '__main__':
    main()