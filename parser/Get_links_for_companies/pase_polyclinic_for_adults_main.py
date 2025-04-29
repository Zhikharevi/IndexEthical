import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/213/moscow/category/polyclinic_for_adults/184106014/?ll=37.609454%2C55.759671&sll=37.609454%2C55.759632"
name_of_file = "moscow_polyclinic_for_adults_links.txt"
# parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file, "/Users/akaki/PycharmProjects/omad_project/chromedriver")
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
