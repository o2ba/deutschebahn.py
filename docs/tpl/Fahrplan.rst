request.Fahrplan
======================================================

Module Fahrplan - v1. Ensure that you are
subscribed to this module.

This module will give you the departure and arrival
boards of **major stations only**. You will have to
reference them with a unique ID that can only be
retrieved from this module.


.. warning::
    Using any of the following functions
    is not recommended. The commands under this module
    will return a dict, list or int instead of
    an object

Rate limiting:
    No standard rate limiting
    (Allows unlimited requests)


def request.get_loc_info
------------------------------------------------------
``def get_loc_info(name: str) -> dict or int``

.. warning::
    It is **highly recommended** to use
    the Station class instead which contains all
    of the information you can retrieve here.

Get information about locations matching the given name
or name fragment. Will return a long list if hits are
found

Arguments:
    name: Name or name fragment of a location

Return if successful:
    * list of dicts. Structure below.

Dictionary structure::

    [
        {
          "locations": [
            {
              "name": "string",
              "lon": 0,
              "lat": 0,
              "id": "string"
            }
          ]
        }
    ]

Return if error:
    * 500, 503 HTTP response status


def request.get_arrival_board
------------------------------------------------------
``def get_arrival_board(id_: int, datetime: str) -> list or int``

Get arrival board at a given location at a given date and time.

.. warning::
    It is **highly recommended** to use
    the Station class instead which contains all
    of the information you can retrieve here.

Arguments:
    * \id_\: ID of location. Use attribute ID from
      the result of the function get_loc_info()
    * datetime: Date and time in ISO-8601 format.
      YYYY-MM-DDTHH:MM:SS. Ex: 2021-05-05T10:30 (German time)

Return if successful:
    * list of dicts. Refer to structure below

Dictionary structure::

    {
      "boards": [
        {
          "name": "string",
          "type": "string",
          "boardId": "string",
          "stopId": "string",
          "dateTime": "string",
          "origin": "string",
          "track": "string",
          "detailsId": "string"
        }
      ]
    }

Return if error:
            * 400, 500, 503 HTTP response status
            * AuthError

def request.get_departure_board
------------------------------------------------------
``def get_departure_board(id_: int, datetime: str) -> list or int``

Get departure board at a given location at a given date and time.

.. warning::
    It is **highly recommended** to use
    the Station class instead which contains all
    of the information you can retrieve here.

Arguments:
    * \id_\: ID of location. Use attribute ID from
      the result of the function get_loc_info()
    * datetime: Date and time in ISO-8601 format.
      YYYY-MM-DDTHH:MM:SS. Ex: 2021-05-05T10:30 (German time)

Return if successful:
    * list of dicts. Refer to structure below

Dictionary structure::

    {
      "boards": [
        {
          "name": "string",
          "type": "string",
          "boardId": "string",
          "stopId": "string",
          "dateTime": "string",
          "origin": "string",
          "track": "string",
          "detailsId": "string"
        }
      ]
    }

Return if error:
    * 400, 500, 503 HTTP response status
    * AuthError


def request.get_journey
------------------------------------------------------
``def get_journey(detailsID: str) -> list or int``

Arguments:
    * detailsID: Details ID of a journey. Use attribute
      detailsId from get_arrival_board or
      get_departure_board

Retrieve details of a journey. The id of the journey
should come from an arrival board or a departure board

Return if successful:
    * list of dicts. Refer to structure below.

Dictionary Structure::

    {
      "train_locs": [
        {
          "stopId": "string",
          "stopName": "string",
          "lat": 0,
          "lon": 0,
          "arrTime": "string",
          "depTime": "string",
          "train": "string",
          "type": "string",
          "operator": "string"
        }
      ]
    }

Return if error:
    * 404, 500, 503
    * AuthError