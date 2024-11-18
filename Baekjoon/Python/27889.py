dic = {'NLCS': 'North London Collegiate School', 'BHA': 'Branksome Hall Asia', 
       'KIS': 'Korea International School', 'SJA': 'St. Johnsbury Academy'}
short = input()
print(dic[short])



# 2 다른사람 풀이 (참고한것)
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