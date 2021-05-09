import deutschebahn as db


# operating station object
class oPoint:
    def __init__(self, json_data):
        # ril100 abbreviation
        self.ril100: str = json_data.get('abbrev')
        self.fullname: str = json_data.get('name')
        self.shortname: str = json_data.get('short')

        self.type: str = json_data['type']

        self.status: str = json_data.get('status')

        self.primaryCode: str = json_data['locationCode']
        self.uic_rics_code: int = json_data['UIC']

        self.region = json_data.get('RB')

    def get_station(self) -> db.Station or None:
        """
        Get station object from opoint. Returns None if not found.

        Warning: Rate limiting (100 req/min standard) may quickly stop
        you from using this command. If you plan on using this for many
        oPoints, consider using db.get_Stations_for_oPoints() instead.
        :return: Station object or None
        """

        StaDa = db.get_stations(ril100=self.ril100)
        les = len(StaDa)

        if les == 0:
            return None
        elif les == 1:
            return StaDa[0]
        else:
            print(f"ERROR!!!!!!!!!!! MORE THAN 1 RESULT FOR {self.fullname}, {self.ril100}")

    def get_region_name(self) -> str or None:
        region_list = ["Ost", "Südost", "Nord", "West", "Mitte", "Südwest", "Süd"]

        return region_list[self.region - 1]
