
"""reads the input and constructs the objects that will generate the output"""

import api_interactions
import outputs
import pprint

def num_of_locations() -> int:
    '''asks the user for how many locations they want'''
    try:
        integer_input = int(input())
        if integer_input < 2:
            print("That is an invalid input")
            return num_of_locations()
        else:
            return integer_input
    except ValueError:
        print("That is an invalid input")
        return num_of_locations()


def address_input(integer_input: int) -> [str]:
    '''asks the user for the addresses they want'''
    address_list = []
    for x in range(integer_input):
        address_input = input()
        address_list.append(address_input)
        if len(address_input) == 0:
            print("That is an invalid address. Please enter all addresses again.")
            return address_input(integer_input)
    return address_list
    

def num_of_outputs() -> int:
    '''ask the user for how many outputs they want'''
    try:
        positive_int_input = int(input())
        if positive_int_input < 1:
            print("That is an invalid input")
            return num_of_outputs()
        else:
            return positive_int_input
    except ValueError:
        print("That is an invalid input")
        return num_of_outputs()
        

def get_output_input(positive_int_input: int) -> ['str']:
    '''creates a list for the outputs desired by the user'''
    output_list = []
    for x in range(positive_int_input):
        output_input = input().upper().strip()
        
        if output_input == "STEPS":
            output_list.append(output_input)

        elif output_input == "TOTALDISTANCE":
            output_list.append(output_input)

        elif output_input == "TOTALTIME":
            output_list.append(output_input)

        elif output_input == "LATLONG":
            output_list.append(output_input)

        elif output_input == "ELEVATION":
            output_list.append(output_input)
            
        else:
            print("That is an invalid input")
            return get_output_input(positive_int_input)

    return output_list

def read_output_list(output_list: list) -> ['classes']:
    '''takes the desired outputs list and returns a list of classes
       relating to the desired outputs'''
    class_list = []
    for item in output_list:
        if item  == "STEPS":
            step_class = outputs.steps()
            class_list.append(step_class)
        if item == "TOTALDISTANCE":
            totaldistance_class = outputs.totaldistance()
            class_list.append(totaldistance_class)
        if item == "TOTALTIME":
            totaltime_class = outputs.totaltime()
            class_list.append(totaltime_class)
        if item == "LATLONG":
            latlong_class = outputs.latlong()
            class_list.append(latlong_class)
        if item == "ELEVATION":
            elevation_class = outputs.elevation()
            class_list.append(elevation_class)
    return class_list




        
def print_copyright() -> None:
    '''prints out the copyright statement'''
    print()
    print("Directions Courtesy of MapQuest; Map Data Copyright " + \
          "OpenStreetMap Contributors.")

def run_user_interface() -> None:
    '''runs the program'''
    try:
        json_result = api_interactions.url_to_json(api_interactions.build_search_url(address_input(num_of_locations())))
        
        if json_result['info']['messages'] != []:
            print("NO ROUTE FOUND")
            return None
        else:
            output_list = get_output_input(num_of_outputs())
            new_list = read_output_list(output_list)
            outputs.read_outputs(new_list, json_result)
    except:
        print("MAPQUEST ERROR")
        return None
    finally:
       print_copyright()

       

if __name__ == '__main__':
    run_user_interface()
