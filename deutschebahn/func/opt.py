from deutschebahn import client
import deutschebahn as db

import requests

url = "https://api.deutschebahn.com/betriebsstellen/v1/betriebsstellen"


def get_oPoints_by_name(search_string: str, return_http_code=False) -> list or int:
    """
    Search for operating stations by name.

    :param search_string: String to search
    :param return_http_code: False by default. Enabling this will return the HTTP status code
                             if it's not 200, rather than returning an empty list. Will return either
                             404 or 416. (Optional Argument)
    :return: list of oStation objects, or empty if no matches.
    """

    @client.authenticated
    def get_json() -> list or int:
        """
        Get the JSON schema rather than objects.

        Note: If the response code is not 200, the dict returned will be of a different model

        :return: [dict, status_code]

        """
        get = requests.get(f'{url}?name={search_string}', headers={"Authorization": f"Bearer {client.__TOKEN__}"})
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
        return [db.oPoint(x) for x in result[1]]


def get_oPoint_by_ril100(ril100: str, return_http_code=False) -> list or int:
    """
    Search for operating station by ril100.

    :param ril100: Ril100 code. Refer to github wiki for more
    :param return_http_code: False by default. Enabling this will return the HTTP status code
                             if it's not 200, rather than returning None. Will return either
                             404 or 416. (Optional Argument)
    :return: list of oStation objects, or empty if no matches.
    """

    @client.authenticated
    def get_json() -> list or int:
        """
        Get the JSON schema rather than an object.

        Note: If the response code is not 200, the dict returned will be of a different model

        :return: [dict, status_code]

        """
        get = requests.get(f'{url}/{ril100}', headers={"Authorization": f"Bearer {client.__TOKEN__}"})
        return [get.status_code, get.json()]

    result = get_json()

    if return_http_code is True and result[1] != 200:
        # if return_http_code is enabled and non-200 result
        return result[0]
    elif result[0] != 200:
        # if return_http_code is disabled and non-200 result
        return None
    else:
        # 200 result
        return db.oPoint(result[1])
