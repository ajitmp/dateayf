import unittest
from dateayf import convert_any_to_your_format

class TestAddFunction(unittest.TestCase):
    your_format_date= "29 April, 1990"

    def test_full_monthname_March(self):
        any_format_date = "March 19, 2024"        
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "19 March, 2024")
    
    def test_full_monthname_April(self):
        any_format_date = "April 10, 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "10 April, 2024")

    def test_full_monthname_May(self):
        any_format_date = "May 22, 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "22 May, 2024")   

    def test_full_monthname_June(self):
        any_format_date = "June 19, 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "19 June, 2024")     


    def test_full_monthname_July(self):
        any_format_date = "July 18, 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "18 July, 2024")                   

    def test_full_monthname_trailing_space(self):
        any_format_date = "June 19, 2024 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "19 June, 2024")

    def test_full_monthname_leading_space_2(self):
        any_format_date = "  June 19, 2024 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "19 June, 2024")

    

    def test_abbr_monthname_Jan(self):
        any_format_date = "Jan. 23, 2024 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "23 January, 2024")

    def test_abbr_monthname_Feb(self):
        any_format_date = "Feb. 2, 2024 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "02 February, 2024")

    def test_abbr_monthname_Aug(self):
        any_format_date = "Aug. 2, 2024 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "02 August, 2024")


    def test_abbr_monthname_Sept(self):
        any_format_date = "Sept. 15, 2023 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "15 September, 2023")

    def test_abbr_monthname_Sep(self):
        any_format_date = "Sep. 15, 2023 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "15 September, 2023")


    def test_abbr_monthname_Oct(self):
        any_format_date = "Oct. 20, 2023 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "20 October, 2023")          
    def test_abbr_monthname_Nov(self):
        any_format_date = "Nov. 17, 2023 "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "17 November, 2023")

    def test_date_suffic_th(self):
        any_format_date = "9th April 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "09 April, 2024")

    def test_date_suffic_rd(self):
        any_format_date = "3rd July 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "03 July, 2024")    

    def test_date_suffic_st(self):
        any_format_date = "1st July 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "01 July, 2024")    


    def test_date_suffic_nd(self):
        any_format_date = "2nd July 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "02 July, 2024")    

    def test_date_abb_month_middle(self):
        any_format_date = "23 Jul 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "23 July, 2024")    

    def test_date_abb_year_last(self):
        any_format_date = "23 Jul 24"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "23 July, 2024") 

    def test_date_abb_year_last_trailing_space(self):
        any_format_date = "23 Jul 24  "
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "23 July, 2024")  

    def test_date_day_th_nd_st_middle(self):
        any_format_date = "July 16th 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "16 July, 2024")    

    def test_date_dot_seperator(self):
        any_format_date = "7.15.2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "15 July, 2024")  

    def test_date_comma_with_time(self):
        any_format_date = "25 July 2013, 9:48"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "25 July, 2013")    

    def test_date_year_comma_with_time(self):
        any_format_date = "January 22, 2020, 6:00"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "22 January, 2020")               

    def test_date_with_dayname(self):
        any_format_date = " • Friday 19th July 2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "19 July, 2024")  

    def test_date_with_forward_slash_sep_month_date_year(self):
        any_format_date = "7/22/2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "22 July, 2024")   
    
    def test_date_with_forward_slash_sep_date_month_year(self):
        any_format_date = "24/07/2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "24 July, 2024")       

    def test_date_with_forward_slash_sep_abb_month(self):
        any_format_date = "23/Jul/2024"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "23 July, 2024")   

    def test_date_with_dayname_and_time(self):
        any_format_date = "Tuesday, 23 July 2024 14:00"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "23 July, 2024")   

    def test_date_abb_month_first_year_last_and_yearwithsingleQuote(self):
        any_format_date = "Apr 30 '24"
        result = convert_any_to_your_format(any_format_date, self.your_format_date)
        self.assertEqual(result, "30 April, 2024") 



    # def test_full_monthname_trailing_space(self):
    #     any_format_date = "June 19, 2024 "
    #     result = convert_any_to_your_format(any_format_date, self.your_format_date)
    #     self.assertEqual(result, "19 June, 2024")


if __name__ == '__main__':
    unittest.main()