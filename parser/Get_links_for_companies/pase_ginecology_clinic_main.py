import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/213/moscow/category/gynecology_clinic/184106100/?ll=37.607324%2C55.766031&sll=37.607323%2C55.765876"
name_of_file = "moscow_ginecology_clinic_links.txt"
# parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file, "/Users/akaki/PycharmProjects/omad_project/chromedriver")
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
