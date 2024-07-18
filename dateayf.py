from datetime import datetime
from dateutil.parser import parse


DATE_FORMATS = ["%m/%d/%Y", "%Y-%m-%d","%m/%d/%Y", "%B %d, %Y","%d %B %Y","%d %B, %Y","%b. %d, %Y","%b %d, %Y"]

def find_suitable_format(input_text_date):  
    for date_format in DATE_FORMATS:
        try:
            if datetime.strptime(input_text_date,date_format):
                return date_format
        except ValueError:
            continue
    return None


def convert_any_to_your_format(input_text_date, target_date):
    #specail case :Python's %b typically matches "Sep", not "Sept.". 
    if input_text_date.lower().startswith("sept"):         
        clean_input_text_date= input_text_date.strip().replace("Sept.", "Sep.")
    else:
        clean_input_text_date= input_text_date.strip()
    clean_target_date = target_date.strip()
    desired_format = find_suitable_format(clean_target_date)
    #print(desired_format)
    input_format = find_suitable_format(clean_input_text_date)    
    #print(input_format)
    if desired_format and input_format:
        # Parse the date string into a datetime object
        parsed_date = datetime.strptime(clean_input_text_date, input_format)
        formatted_date = parsed_date.strftime(desired_format )
        return formatted_date
    else:
        return "Date format not found."


if __name__=='__main__':
    input_date = "Sept. 15, 2023"
    #print(parse(input_date))
    target_date= "29 April, 1990"
    #print(parse(target_date))
    print(convert_any_to_your_format(input_date, target_date))