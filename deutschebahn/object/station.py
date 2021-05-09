

class Station:
    def __init__(self, json_data):
        self.fullname = json_data.get('name')
        self.number = json_data.get('number')

        self.ril100 = None

        for identifier in json_data['ril100Identifiers']:
            if identifier['isMain'] is True:
                self.ril100 = identifier['rilIdentifier']



