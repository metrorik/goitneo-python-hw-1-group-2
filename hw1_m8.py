
from datetime import datetime


def get_birthdays_per_week(users):
    birt_dict = {}
    formatted_output = ""
    curr_data = datetime.today().date()
    curr_year = datetime.today().year

    for user in users:

        usr_name = user["name"]
        birt_data = user["birthday"].date()
        birt_in_this_year = birt_data.replace(year=curr_year)
        birt_in_this_year_of_week = birt_in_this_year.strftime('%A')

        if birt_in_this_year < curr_data:                               # д.р. в этом году уже был
            birt_in_this_year = birt_data.replace(year=curr_year+1)
        delta_days = (birt_in_this_year - curr_data).days
        if delta_days < 7:                                              # д.р. на текущей неделе
            if birt_in_this_year.weekday() < 5:                         # не попадает на выходные
                if birt_in_this_year_of_week not in birt_dict:
                    birt_dict[birt_in_this_year_of_week] = []
                birt_dict[birt_in_this_year_of_week].append(usr_name)                   
            else:                                                       # попадает на выходные, поздравить в понедельник
                if "Monday" not in birt_dict:
                    birt_dict["Monday"] = []
                birt_dict["Monday"].append(usr_name)

    for day, names in sorted(birt_dict.items(), key=lambda x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(x[0])):
        formatted_output += f"{day}: {', '.join(names)}\n"
    
    print(formatted_output)    
    return formatted_output
