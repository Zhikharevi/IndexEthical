import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/213/moscow/category/family_planning_clinic/43413743342/?ll=37.604202%2C55.743179&sll=37.604202%2C55.743024&z=11"
name_of_file = "moscow_family_planing_clinic_links.txt"
parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
