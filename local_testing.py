import deutschebahn as db
import deutschebahn.request

from pprint import pprint

""""
def main():
    db.Auth("02fa40438f2b58a346830b8129cbd891")
    route = input("Station name, or part of it: ")
    hits = db.request.get_ostations_query(route)
    for e, element in enumerate(hits):
        print(f"{e}: {element['name']}")

    select = int(input("Please select the correct station: "))
    if type(select) == int:
        chosen = hits[select]
        abbrev = chosen['abbrev']
        pprint(db.request.get_station_pattern(abbrev))
        eva = db.request.get_station_pattern(abbrev)['@eva']

        pprint(db.request.get_planned_data(eva, '210507', '09'))

"""

if __name__ == '__main__':
    db.Auth("02fa40438f2b58a346830b8129cbd891")
    st = db.request.get_stations_master(limit=10000)

    for x in st["result"]:
        try:
            pprint(x["regionalbereich"])
        except KeyError:
            continue

