
def special_school_name(name):
    school_dict = {
        "NLCS": "North London Collegiate School",
        "BHA": "Branksome Hall Asia",
        "KIS": "Korea International School",
        "SJA": "St. Johnsbury Academy"
    }
    
    return school_dict[name]


if __name__ == "__main__":
    school_name = input()
    
    print(special_school_name(name=school_name))
    
