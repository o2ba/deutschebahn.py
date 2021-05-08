request.Betriebsstellenü
=========================================================

Module Betriebsstellen - v1. Ensure that you are
subscribed to this module.

.. warning::
    Using any of the following functions
    is not recommended. The commands under this module
    will return a dict, list or int instead of
    an object

Rate limiting:
    Standard rate limit is 10 per minute.

def request.get_ostations_query
------------------------------------------------------
``get_ostations_query(value: str) -> list or int``

.. warning::
    It is **highly recommended** to use
    find_station instead. This function will
    return a dict, rather than a class.

Looks for station(s) by station name or part of it
with a given value. Must be authenticated before use

Arguments:
    value (str): Keyword to search for in the database of
    stations

Returns if successful (Response code 200):
    List of matches::

        [
          {
            "abbrev": "string",
            "name": "string",
            "short": "string",
            "type": "Abzw",
            "status": "in use",
            "locationCode": "string",
            "UIC": "string",
            "RB": 0,
            "validFrom": "string",
            "validTill": "string",
            "id": 0,
            "timeTableRelevant": true,
            "borderStation": true
          }
        ]

Returns if failed:
    * 404, 416 HTTP response status
    * client.AuthError


def request.get_ostations_info
------------------------------------------------------

``get_ostations_info(abbreviation: str) -> dict or int``

.. warning::
    It is **highly recommended** to use
    get_station instead. This function will
    return a dict, rather than a class.

Returns station info given a station abbreviation.
*If you do not know the station abbreviation, consider
using get_ostations_query() function instead.*

Arguments:
    abbreviation (str): Station abbreviation
    (standardized) to refer to a single unique station.

Returns if successful (Response code 200):
    Dict of the match::

        {
          "abbrev": "string",
          "name": "string",
          "short": "string",
          "type": "Abzw",
          "status": "in use",
          "locationCode": "string",
          "UIC": "string",
          "RB": 0,
          "validFrom": "string",
          "validTill": "string",
          "id": 0,
          "timeTableRelevant": true,
          "borderStation": true
        }

Returns if failed:
    * 404, 416 HTTP response status
    * client.AuthError: if not authenticated