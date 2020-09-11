import requests

from bs4 import BeautifulSoup
url = "https://bashesk.ru/upload/iblock/f0f/ПУНЦЭМ_до 670кВт_октябь  2019.xls"

# <div class="row wide-dwn-itm no-gutters">
#  		 	<div class="col-10">
#  		 		 <a href="./812638/">Предельные уровни нерегулируемых цен на электрическую энергию (мощность), поставляемую потребителям (покупателям) ООО "ЭСКБ", (с максимальной мощностью энергопринимающих устройств до 670 кВт) за август 2019 года</a>
#  		 	</div>
#  		 	<div class="col-2">
#  		 		 		 		<a href="/upload/iblock/f16/ПУНЦЭМ_до 670кВт_август  2019.xls">
# 	 		 		<img src="/local/templates/bashesk_new1/img/icon-doc-xls.png">
# 	 		 		<div>Скачать документ</div>
#  		 		</a>
#  		 	</div>
#  		 </div>


site_url = "https://bashesk.ru/corporate/tariffs/unregulated/limits/?sort_by=NAME&sort_order=asc&filter_name=&filter_date_from=01.07.2019&filter_date_to=01.07.2020"

def get_xlsx(url):
    with requests.Session() as session:
        resp = session.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        xls_list=[]
        for i in range(13):
            xls_list.append(str(soup.find_all(class_="row wide-dwn-itm no-gutters")[i].find(class_="col-2").find_all('a')[0]).split('href="')[1].split('">')[0])
        return xls_list

def main():
    print(get_xlsx(site_url))


if __name__ == "__main__":
    main()