import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/213/moscow/category/children_hospital/184105958/?ll=37.549215%2C55.756555&sll=37.549215%2C55.755935&z=10"
name_of_file = "moscow_children_hospital_links.txt"
# parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file, "/Users/akaki/PycharmProjects/omad_project/chromedriver")
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
