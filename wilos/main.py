import click
import os
import requests
import sys
import json

from wilos.exceptions import IncorrectParametersException, APIErrorException
from wilos.writers import get_writer

FORECAST_BASE_URL = 'https://api.forecast.io/forecast/'
GOOGLE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"

try:
    forecast_api_token = os.environ['WILOS_CLI_FORECAST_API_TOKEN']
    google_api_token = os.environ['WILOS_CLI_GOOGLE_API_TOKEN']
except KeyError:
    from wilos.config import config
    forecast_api_token = config.get('WILOS_CLI_FORECAST_API_TOKEN')
    google_api_token = config.get('WILOS_CLI_GOOGLE_API_TOKEN')

if not forecast_api_token:
    print ('No Forecast.io API Token detected. Please visit {0} and get an API Token, '
           'which will be used by the WILOS CLI to get access to the data'
           .format(FORECAST_BASE_URL))
    sys.exit(1)

if not google_api_token:
    print ('No Google Maps API Token detected. Please visit https://console.developers.google.com/apis/ and get an API Token, '
           'which will be used by the WILOS CLI to get access to the data')
    sys.exit(1)

forecast_headers = {
    'X-Auth-Token': forecast_api_token
}

def get_coordinates(loc):
    payload = {'key': google_api_token, 'address': loc}
    req = requests.get(GOOGLE_BASE_URL, params=payload)
    if req.status_code == requests.codes.ok:
        geocode = req.json()
        if geocode['results'] is not None:
            address = geocode['results'][0]['formatted_address']
            coordinates = geocode['results'][0]['geometry']['location']
            res = {
                "address": address,
                "coordinates": coordinates
            }
            return res
    else:
        click.secho("There was problem during geoencoding", fg="red", bold=True)


def get_live_weather(lat, lon, writer):
    """Gets the live weather via lat and long"""
    requrl = FORECAST_BASE_URL+forecast_api_token+'/'+str(lat)+','+str(lon)
    req = requests.get(requrl)
    if req.status_code == requests.codes.ok:
        weather = req.json()
        if not weather['currently']:
            click.secho("No live weather currently", fg="red", bold=True)
            return
        writer.live_weather(weather)
    else:
        click.secho("There was problem getting live weather", fg="red", bold=True)

@click.command()
@click.option('--lat', is_flag=False, help="Latitude for location")
@click.option('--lon', is_flag=False, help="Longitude for location")
@click.option('--loc', is_flag=False, help="General Location (String)")
def main(lat, lon, loc):
    """W.I.L.O.S: What's it like outside?"""
    writer = get_writer()

    try:
        if (not lat or not lon) and (not loc):
            raise IncorrectParametersException('Please specify a latitude, longitude, or location'
                                               'Example: wilos --lat=19.8968 --lon=155.5828 --loc="hawaii"')
        if lat is not None and long is not None:
            get_live_weather(lat, lon, writer)
        elif loc is not None:
            loc_data = get_coordinates(loc)
            writer.title(loc_data['address'])
            get_live_weather(loc_data['coordinates']['lat'],
                             loc_data['coordinates']['lng'],
                             writer)

    except IncorrectParametersException as e:
        click.secho(e.message, fg="red", bold=True)

if __name__ == '__main__':
    main()
