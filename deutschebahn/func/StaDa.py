from deutschebahn import client
import deutschebahn as db

import requests

url = "https://api.deutschebahn.com/stada/v2"

__STATIONS_LIST__ = None


def get_Stations(offset: int = 0, limit: int = 1000, searchstring: str = None, category: str = "1-7",
                 federalstate: str = None, eva: str = None,
                 ril100: str = None, logicaloperator: str = "AND", return_http_code: bool = False) -> int or list:
    """

    Get a list of stations from the StaDa module. This will return a list of station objects if matches are
    found, otherwise it will return an empty list, or the return code if return_http_code is true.

    :param offset:
        Offset of the first hit returned in the QueryResult object with respect to all hits returned by the query.
        If this parameter is omitted, it will be set to 0 internally.

    :param limit:
        The maximum number of hits to be returned by that query. Default is 1000, maximum is 10000.

    :param searchstring:
        String to search for a station name. The wildcards (indicating an arbitrary number of characters) and ?
        (indicating one single character) can be used in the search pattern. A comma separated list of station names is
        also supported (e.g. searchstring=hamburg,berlin*).

    :param category:
        Filter by station category. Category ranges are supported as well as lists of categories
        (e.g. category=2-4 or category=1,3-5). The category must be between 1 and 7 otherwise a parameter exception
        is returned.

    :param federalstate:
        Filter by German federal state. Lists of federal states are also supported (e.g. federalstate=bayern,hamburg).
        Wildcards are not allowed here.

    :param eva:
        Filter by EVA number. Wildcards are not allowed here.

    :param ril100:
        Filter by Ril100-identifier. Wildcards are not allowed here.

    :param logicaloperator:
        Logical operator to combine query parameters (default=AND).
        See above for further details. Allowed values: or, and

    :param return_http_code: False by default. Enabling this will return the HTTP status code
                             if it's not 200, rather than returning an empty list. (Optional Argument)

    :return: list of oStation objects, or empty if no matches.
    """

    def get_json():
        get = requests.get(f'{url}/stations',
                           headers={"Authorization": f"Bearer {client.__TOKEN__}"},
                           params={
                               "offset": offset,
                               "limit": limit,
                               "searchstring": searchstring,
                               "category": category,
                               "federalstate": federalstate,
                               "eva": eva,
                               "ril": ril100,
                               "logicaloperator": logicaloperator
                           })

        return [get.status_code, get.json()]

    result = get_json()

    if return_http_code is True and result[0] != 200:
        # if return_http_code is enabled and non-200 result
        return result[0]
    elif result[0] != 200:
        # if return_http_code is disabled and non-200 result
        return []
    else:
        # 200 result
        return [db.Station(x) for x in result[1].get("result")]


def get_Stations_for_oPoints(oPoint_list: [db.oPoint], force_update=False, force_delete=False):
    """
    If you have a large number of oPoint objects for which you wish to get Station objects,
    but using oPoint.get_station() would send many requests causing you to hit your rate limit,
    you may instead pass a list of oPoints to this function to retrieve a list of Stations where
    found.

    This function will retrieve every station from the StaDa module, and will look for a match
    by their ril100 numbers. The returned list will be indexed in parallel to the input list,
    with None as a value if no corresponding station was found.

    This function will store the values returned from the API (list of every station), and will
    not call the API if the list stored is already populated. It will also not delete this list
    once the search is finished. You may change this with the optional boolean params force_update
    and force_delete

    :param oPoint_list: A list of oPoint objects. This function will not check if the input is correct.

    :param force_update: This will call force the function to call the StaDa API to retrieve every station
                         even if it has been called before and it is stored in a local list. Doing this
                         will ensure that if there's an updated entry to the StaDa database, you would
                         be able to retrieve it. Please note that getting a return value from the API
                         takes a considerable amount of time

    :param force_delete: This will force the values to be deleted at the end of this function, freeing
                         up memory.

    :return: A list of Station objects parralel to the indexing of the oPoint_list param. If no match
             is found, None will be the value.
    """

    global __STATIONS_LIST__

    if __STATIONS_LIST__ is None or force_update is True:
        gSt = get_Stations(limit=10000)
        __STATIONS_LIST__ = gSt if gSt != [] else None

    # List that will be populated with the matches
    result_list = []

    # if not None
    if __STATIONS_LIST__:

        # LOOP THROUGH STATIONS LIST

        for element in oPoint_list:

            # Loop through __STATIONS_LIST_ checking for a match with the current oPoint object. Return None if not
            # found.
            search = next((item for item in __STATIONS_LIST__ if element.ril100 is not None and item.ril100 == element.ril100), None)

            result_list.append(search)
    else:
        raise Exception("Hello World")

    return result_list



