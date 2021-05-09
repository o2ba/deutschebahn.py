"""
Deutsche Bahn API Wrapper

:copyright: (c) 2021 Bade Obari
:license: MIT, see LICENSE for more details.

"""

from .client import *
from .object.opoint import oPoint, Type, Region
from .object.station import Station

from .func.Betriebsstellen import get_oPoints_by_name, get_oPoint_by_ril100
from .func.StaDa import get_stations, get_Stations_for_oPoints


