request.Timetables
=========================================================


def request.get_station_pattern
------------------------------------------------------
``def get_station_pattern(pattern: str, XML: bool = False)
-> dict or int``

Get information about a given station

Arguments:
    * pattern: Station name (prefix), EVA number,
      ds100/rl100 code.
    * XML: Placeholder for future implementation

Return if success:
    * custom dict

Dictionary::

    {
        "@p": str,
        "@meta": str,
        "@name": str,
        "@eva": str,
        "@ds100": str,
        "@creationts": str,
        "@db": str
    }


Description:
    * p: List of platforms (Optional) (separated by \|\)
    * meta: List of meta stations (Optional) (separated by \|\)
    * name: Station name
    * eva: EVA station number
    * ds100: DS100 Station code
    * db: Flag for stations of DB (Optional)
    * createionts: Creation time (Optional)


def request.get_planned_data
------------------------------------------------------
``def get_planned_data(evaNo: int, date: str, hour: str)
-> list or int``

Arguments:
    * evaNo: Station EVA number
    * date: Date format YYMMDD
    * hour: Hour in format HH

Return if success:
    * custom list of dicts

Dictionary::

    {
        '@station': str,
        's' :[{
                '@id': str,
                'ar': {
                    '@l': str,
                    '@pp': str,
                    '@ppth': str,
                    '@pt': str
                },
                'dp': {
                    '@l': str,
                    '@pp': str,
                    '@ppth': str,
                    '@pt': str
                },
                'tl: {
                    '@c': str,
                    '@f': str,
                    '@n': str,
                    '@o': str,
                    '@t': str
                }

            }]

Return if fail:
    # TODO

def request.get_known_changes, def request.get_recent_changes
------------------------------------------------------
``def get_known_changes(evaNo: int) -> list or int``
``def get_recent_changes(evaNo: int) -> list or int``

Gets known changes and recent changes respectively

Arguments:
    * evaNo: Station EVA number

Return if success:
    * dict

Dictionary::

    {
          "station": "string",
          "eva": 0,
          "s": [
            {
              "id": "string",
              "eva": 0,
              "tl": {
                "f": "string",
                "t": "p",
                "o": "string",
                "n": "string",
                "c": "string"
              },
              "ref": {
                "tl": {
                  "f": "string",
                  "t": "p",
                  "o": "string",
                  "n": "string",
                  "c": "string"
                },
                "rt": [
                  {
                    "f": "string",
                    "t": "p",
                    "o": "string",
                    "n": "string",
                    "c": "string"
                  }
                ]
              },
              "ar": {
                "ppth": "string",
                "cpth": "string",
                "pp": "string",
                "cp": "string",
                "pt": "string",
                "ct": "string",
                "ps": "p",
                "cs": "p",
                "hi": 0,
                "clt": "string",
                "wings": "string",
                "tra": "string",
                "pde": "string",
                "cde": "string",
                "dc": 0,
                "l": "string",
                "m": [
                  {
                    "id": "string",
                    "t": "h",
                    "from": "string",
                    "to": "string",
                    "c": 0,
                    "int": "string",
                    "ext": "string",
                    "cat": "string",
                    "ec": "string",
                    "ts": "string",
                    "pr": 1,
                    "o": "string",
                    "elnk": "string",
                    "del": 0,
                    "dm": [
                      {
                        "t": "s",
                        "n": "string",
                        "int": "string",
                        "ts": "string"
                      }
                    ],
                    "tl": [
                      {
                        "f": "string",
                        "t": "p",
                        "o": "string",
                        "n": "string",
                        "c": "string"
                      }
                    ]
                  }
                ]
              },
              "dp": {
                "ppth": "string",
                "cpth": "string",
                "pp": "string",
                "cp": "string",
                "pt": "string",
                "ct": "string",
                "ps": "p",
                "cs": "p",
                "hi": 0,
                "clt": "string",
                "wings": "string",
                "tra": "string",
                "pde": "string",
                "cde": "string",
                "dc": 0,
                "l": "string",
                "m": [
                  {
                    "id": "string",
                    "t": "h",
                    "from": "string",
                    "to": "string",
                    "c": 0,
                    "int": "string",
                    "ext": "string",
                    "cat": "string",
                    "ec": "string",
                    "ts": "string",
                    "pr": 1,
                    "o": "string",
                    "elnk": "string",
                    "del": 0,
                    "dm": [
                      {
                        "t": "s",
                        "n": "string",
                        "int": "string",
                        "ts": "string"
                      }
                    ],
                    "tl": [
                      {
                        "f": "string",
                        "t": "p",
                        "o": "string",
                        "n": "string",
                        "c": "string"
                      }
                    ]
                  }
                ]
              },
              "m": [
                {
                  "id": "string",
                  "t": "h",
                  "from": "string",
                  "to": "string",
                  "c": 0,
                  "int": "string",
                  "ext": "string",
                  "cat": "string",
                  "ec": "string",
                  "ts": "string",
                  "pr": 1,
                  "o": "string",
                  "elnk": "string",
                  "del": 0,
                  "dm": [
                    {
                      "t": "s",
                      "n": "string",
                      "int": "string",
                      "ts": "string"
                    }
                  ],
                  "tl": [
                    {
                      "f": "string",
                      "t": "p",
                      "o": "string",
                      "n": "string",
                      "c": "string"
                    }
                  ]
                }
              ],
              "hd": [
                {
                  "ts": "string",
                  "ar": "string",
                  "dp": "string",
                  "src": "L",
                  "cod": "string"
                }
              ],
              "hpc": [
                {
                  "ts": "string",
                  "ar": "string",
                  "dp": "string",
                  "cot": "string"
                }
              ],
              "conn": [
                {
                  "id": "string",
                  "ts": "string",
                  "eva": 0,
                  "cs": "w",
                  "ref": {},
                  "s": {}
                }
              ],
              "rtr": [
                {
                  "rt": {
                    "id": "string",
                    "c": true,
                    "rtl": {
                      "n": "string",
                      "c": "string"
                    },
                    "sd": {
                      "i": 0,
                      "pt": "string",
                      "eva": 0,
                      "n": "string"
                    },
                    "ea": {
                      "i": 0,
                      "pt": "string",
                      "eva": 0,
                      "n": "string"
                    }
                  },
                  "rts": "b"
                }
              ]
            }
          ],
          "m": [
            {
              "id": "string",
              "t": "h",
              "from": "string",
              "to": "string",
              "c": 0,
              "int": "string",
              "ext": "string",
              "cat": "string",
              "ec": "string",
              "ts": "string",
              "pr": 1,
              "o": "string",
              "elnk": "string",
              "del": 0,
              "dm": [
                {
                  "t": "s",
                  "n": "string",
                  "int": "string",
                  "ts": "string"
                }
              ],
              "tl": [
                {
                  "f": "string",
                  "t": "p",
                  "o": "string",
                  "n": "string",
                  "c": "string"
                }
              ]
            }
          ]
    }

Return if fail:
    * 400, 404, 410
    * AuthError



