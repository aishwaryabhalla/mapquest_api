
"""implements various outputs as a separate class"""

import api_interactions


class steps:
    ''' information about steps taken from api_interactions '''
    def output(self, json):
        ''' prints out steps info '''
        print()
        print("DIRECTIONS:")
        for line in api_interactions.steps_parse(json):
            print(line)


class totaldistance:
    ''' information about total distance taken from api_interactions '''
    def output(self, json):
        ''' prints out total distance info '''
        print()
        distance = round(api_interactions.distance_parse(json))
        print("TOTAL DISTANCE:", distance, "miles")



class totaltime:
    ''' information about total time taken from api_interactions '''
    def output(self, json):
        ''' prints out total time info '''
        print()
        time = round((api_interactions.time_parse(json))/60)
        print("TOTAL TIME:", time, "minutes")



class latlong:
    ''' information about latitude/longitude taken from api_interactions '''
    def output(self, json):
        ''' prints out latitude/longitude info '''
        print()
        print("LATLONGS")
        tup_list = api_interactions.latlongs_parse(json)
        for tup in tup_list:
            if tup[0] < 0 and tup[1] < 0:
                print(round(tup[0], 2), "S", round(tup[1], 2), "W")
            elif tup[0] < 0 and tup[1] > 0:
                print(round(tup[0], 2), "S", round(tup[1], 2), "E")
            elif tup[0] > 0 and tup[1] < 0:
                print(round(tup[0], 2), "N", round(tup[1], 2), "W")
            elif tup[0] > 0 and tup[1] > 0:
                print(round(tup[0], 2), "N", round(tup[1], 2), "E")


class elevation:
    ''' information about elevation taken from api_interactions '''
    def output(self, json):
        ''' prints out elevation info '''
        print()
        print("ELEVATIONS")
        url_list = api_interactions.elevation_url(api_interactions.latlongs_parse(json))
        for every_url in url_list:
            elev_json = api_interactions.url_to_json(every_url)
            elevation = api_interactions.elevations_parse(elev_json)
            for height in elevation:
                print(round(int(height)*3.28084), "feet")
        
def read_outputs(output_list: list, json: 'json') -> None:
    '''duck-typing for classes so that all classes go through output'''
    for output_str in output_list:
        output_str.output(json)
    return None
