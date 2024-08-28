from datetime import datetime
import re
#from dateutil.parser import parse


DATE_FORMATS = ["%d.%m.%Y", "%b %d '%y", "%m/%d/%Y", "%d/%b/%Y", "%Y-%m-%d","%m/%d/%Y","%d/%m/%Y", "%B %d, %Y", "%B %d %Y", "%d %B %Y","%d %B, %Y","%b. %d, %Y","%b %d, %Y","%d %b %Y","%d %b %y", "%d %b, %Y", "%m.%d.%Y","%m/%d/%Y"]

def find_suitable_format(input_text_date):
    for date_format in DATE_FORMATS:
        try:
            if datetime.strptime(input_text_date,date_format):
                return date_format
        except ValueError:
            continue
    return None

def __clean_st_nd_rd_from_date_old(input_date_str):
    if "th" in input_date_str :
        return input_date_str.replace("th","")
    elif "rd" in input_date_str :
        return input_date_str.replace("rd","")
    elif "st" in input_date_str :
        return input_date_str.replace("st","")
    elif "nd" in input_date_str :
        return input_date_str.replace("nd","")
    else:
        return input_date_str.strip()

def __clean_st_nd_rd_from_date(input_date_str):
    #print(input_date_str)
    # Regular expression pattern to match any digit followed by "st", "nd", "rd", or "th"
    pattern = r'(\d+)(st|nd|rd|th)'
    if re.search(pattern,input_date_str):
        result = re.sub(pattern, r'\1', input_date_str)
        #print(result)
        return result
    else:
        return input_date_str.strip()





def clean_date_str(input_date_str):
    #print(input_date_str)
    input_date_str = __clean_st_nd_rd_from_date(input_date_str)
    #print(input_date_str)
    if input_date_str.lower().startswith("sept"):
        return input_date_str.strip().replace("Sept.", "Sep.")
    elif ":" in input_date_str and "day" in input_date_str:
        #"Tuesday, 23 July 2024 14:00"
        return " ".join(input_date_str.split(',')[1].split()[:-1])
    elif ":" in input_date_str:
        #"17 September 2013, 8:33"
        return " ".join(input_date_str.split(',')[:-1])
    elif "day" in input_date_str:
        # • Friday 19th July 2024
        return " ".join(input_date_str.split()[2:])
    else:
        return input_date_str.strip()


def convert_any_to_your_format(input_text_date, target_date):
    #specail case :Python's %b typically matches "Sep", not "Sept.".
    # if input_text_date.lower().startswith("sept"):
    #     clean_input_text_date= input_text_date.strip().replace("Sept.", "Sep.")
    # else:
    #     clean_input_text_date= input_text_date.strip()
    clean_input_text_date = clean_date_str(input_text_date)
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