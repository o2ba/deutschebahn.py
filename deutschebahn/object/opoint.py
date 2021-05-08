import deutschebahn as db

class Region:
    def __init__(self, region_id: int):
        self.id = region_id


class Type:
    def __init__(self, st: str):
        self.st = st


# operating station object
class oPoint:
    def __init__(self, json_data):
        # ril100 abbreviation
        self.ril100: str = json_data['abbrev']
        self.fullname: str = json_data['name']
        self.shortname: str = json_data['short']

        self.type: Type = Type(json_data['type'])

        self.status: str = json_data.get('status')

        self.primaryCode: str = json_data['locationCode']
        self.uic_rics_code: int = json_data['UIC']

        self.region: Region = Region(json_data.get('RB'))


    def get_station(self) -> db.station:
        """
        Get station object
        :return:
        """