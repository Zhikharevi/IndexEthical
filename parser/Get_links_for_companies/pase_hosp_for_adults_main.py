import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/213/moscow/category/hospital/184105956/?ll=37.650320%2C55.743619&sll=37.590839%2C55.753645&sspn=1.441407%2C0.555897&z=10.96"
name_of_file = "moscow_hosp_for_adults_links.txt"
parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
