import parse_clinics_algo_main
import parse_clinics_algo_extra


link = "https://yandex.ru/maps/?display-text=%D0%90%D0%BC%D0%B1%D1%83%D0%BB%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F%2C%20%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BF%D1%83%D0%BD%D0%BA%D1%82%2C%20%D0%BC%D0%B5%D0%B4%D0%BF%D1%83%D0%BD%D0%BA%D1%82&ll=37.590839%2C55.753645&mode=search&sll=37.611735%2C55.742076&sspn=1.411743%2C0.544619&text=category_id%3A%28184105950%29&z=9.97"
name_of_file = "moscow_medpunct_links.txt"
parse_clinics_algo_main.get_links_on_stream_of_company(link, name_of_file)
# parse_clinics_algo_extra.get_links_on_stream_of_company(link, name_of_file)
