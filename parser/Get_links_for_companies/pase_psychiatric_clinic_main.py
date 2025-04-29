import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/213/moscow/category/psychiatric_clinic/16337527195/?ll=37.697284%2C55.784104&sll=37.697284%2C55.781625"
name_of_file = "moscow_psychiatric_clinic_links.txt"
# parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file, "/Users/akaki/PycharmProjects/omad_project/chromedriver")
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
