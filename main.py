from dateutil import parser
from datetime import datetime
from requests import Session, get
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import requests

title = 'Kuromon Ichiba —\xa0Is This Famous Seafood Market In Osaka A Tourist Trap Or Worth The Hype?'

print(title.find('\u2013'))

# def scrap():
#   url = "https://en.wikipedia.org/wiki/List_of_cuisines"
#   resp =  requests.get(url)
#   cuisineHTMLData = '''
#   <ul><li><a href="/wiki/Afghan_cuisine" title="Afghan cuisine">Afghan</a></li>
# <li><a href="/wiki/Albanian_cuisine" title="Albanian cuisine">Albanian</a></li>
# <li><a href="/wiki/Algerian_cuisine" title="Algerian cuisine">Algerian</a></li>
# <li><a href="/wiki/American_cuisine" title="American cuisine">American</a>
# <ul><li><a href="/wiki/American_Chinese_cuisine" title="American Chinese cuisine">American Chinese</a></li>
# <li><a href="/wiki/California_cuisine" title="California cuisine">California</a></li>
# <li><a href="/wiki/Greek-American_cuisine" title="Greek-American cuisine">Greek American</a></li>
# <li><a href="/wiki/Cuisine_of_Hawaii" title="Cuisine of Hawaii">Hawaiian</a></li>
# <li><a href="/wiki/Italian-American_cuisine" title="Italian-American cuisine">Italian American</a></li>
# <li><a href="/wiki/Louisiana_Creole_cuisine" title="Louisiana Creole cuisine">Louisiana Creole</a></li>
# <li><a href="/wiki/New_American_cuisine" title="New American cuisine">New American</a></li>
# <li><a href="/wiki/Cuisine_of_New_England" title="Cuisine of New England">New England</a></li>
# <li><a href="/wiki/Cuisine_of_the_Pennsylvania_Dutch" title="Cuisine of the Pennsylvania Dutch">Pennsylvania Dutch</a></li>
# <li><a href="/wiki/Puerto_Rican_cuisine" title="Puerto Rican cuisine">Puerto Rican</a></li>
# <li><a href="/wiki/Soul_food" title="Soul food">Soul food</a></li></ul></li>
# <li><a href="/wiki/Angolan_cuisine" title="Angolan cuisine">Angolan</a></li>
# <li><a href="/wiki/Argentine_cuisine" title="Argentine cuisine">Argentine</a></li>
# <li><a href="/wiki/Armenian_cuisine" title="Armenian cuisine">Armenian</a></li>
# <li><a href="/wiki/Australian_cuisine" title="Australian cuisine">Australian</a></li>
# <li><a href="/wiki/Austrian_cuisine" title="Austrian cuisine">Austrian</a></li>
# <li><a href="/wiki/Azerbaijani_cuisine" title="Azerbaijani cuisine">Azerbaijani</a></li>
# <li><a href="/wiki/Bahraini_cuisine" title="Bahraini cuisine">Bahraini</a></li>
# <li><a href="/wiki/Bangladeshi_cuisine" title="Bangladeshi cuisine">Bangladeshi</a>
# <ul><li><a href="/wiki/Sylheti_cuisine" title="Sylheti cuisine">Sylheti</a></li></ul></li>
# <li><a href="/wiki/Barbadian_cuisine" title="Barbadian cuisine">Barbadian</a></li>
# <li><a href="/wiki/Belarusian_cuisine" title="Belarusian cuisine">Belarusian</a></li>
# <li><a href="/wiki/Belgian_cuisine" title="Belgian cuisine">Belgian</a></li>
# <li><a href="/wiki/Belizean_cuisine" title="Belizean cuisine">Belizean</a></li>
# <li><a href="/wiki/Benin_cuisine" title="Benin cuisine">Beninese</a></li>
# <li><a href="/wiki/Bhutanese_cuisine" title="Bhutanese cuisine">Bhutanese</a></li>
# <li><a href="/wiki/Bolivian_cuisine" title="Bolivian cuisine">Bolivian</a></li>
# <li><a href="/wiki/Bosnia_and_Herzegovina_cuisine" title="Bosnia and Herzegovina cuisine">Bosnian-Herzegovinian</a></li>
# <li><a href="/wiki/Botswana_cuisine" title="Botswana cuisine">Botswana</a></li>
# <li><a href="/wiki/Brazilian_cuisine" title="Brazilian cuisine">Brazilian</a></li>
# <li><a href="/wiki/British_cuisine" title="British cuisine">British</a>
# <ul><li><a href="/wiki/English_cuisine" title="English cuisine">English</a></li>
# <li><a href="/wiki/Northern_Irish_cuisine" title="Northern Irish cuisine">Northern Irish</a></li>
# <li><a href="/wiki/Scottish_cuisine" title="Scottish cuisine">Scottish</a></li>
# <li><a href="/wiki/Welsh_cuisine" title="Welsh cuisine">Welsh</a></li></ul></li>
# <li><a href="/wiki/Bruneian_cuisine" title="Bruneian cuisine">Bruneian</a></li>
# <li><a href="/wiki/Bulgarian_cuisine" title="Bulgarian cuisine">Bulgarian</a></li>
# <li><a href="/wiki/Burkinabe_cuisine" title="Burkinabe cuisine">Burkinabé</a></li>
# <li><a href="/wiki/Burmese_cuisine" title="Burmese cuisine">Burmese</a></li>
# <li><a href="/wiki/Burundian_cuisine" title="Burundian cuisine">Burundian</a></li>
# <li><a href="/wiki/Cambodian_cuisine" title="Cambodian cuisine">Cambodian</a></li>
# <li><a href="/wiki/Cameroonian_cuisine" title="Cameroonian cuisine">Cameroonian</a></li>
# <li><a href="/wiki/Canadian_cuisine" title="Canadian cuisine">Canadian</a>
# <ul><li><a href="/wiki/Cuisine_of_Quebec" title="Cuisine of Quebec">Québécois</a></li>
# <li><a href="/wiki/Acadian_cuisine" title="Acadian cuisine">Acadian</a></li></ul></li>
# <li><a href="/wiki/Cuisine_of_the_Central_African_Republic" title="Cuisine of the Central African Republic">Central African Republic</a></li>
# <li><a href="/wiki/Chadian_cuisine" title="Chadian cuisine">Chadian</a></li>
# <li><a href="/wiki/Chilean_cuisine" title="Chilean cuisine">Chilean</a></li>
# <li><a href="/wiki/Chinese_cuisine" title="Chinese cuisine">Chinese</a>
# <ul><li><a href="/wiki/Cantonese_cuisine" title="Cantonese cuisine">Cantonese</a></li>
# <li><a href="/wiki/Chinese_Islamic_cuisine" title="Chinese Islamic cuisine">Chinese Islamic</a></li>
# <li><a href="/wiki/Hong_Kong_cuisine" title="Hong Kong cuisine">Hong Kong</a></li>
# <li><a href="/wiki/Macanese_cuisine" title="Macanese cuisine">Macanese</a></li>
# <li><a href="/wiki/Tibetan_cuisine" title="Tibetan cuisine">Tibetan</a></li></ul></li>
# <li><a href="/wiki/Colombian_cuisine" title="Colombian cuisine">Colombian</a></li>
# <li><a href="/wiki/Congolese_cuisine" title="Congolese cuisine">Congolese</a></li>
# <li><a href="/wiki/Croatian_cuisine" title="Croatian cuisine">Croatian</a></li>
# <li><a href="/wiki/Cuban_cuisine" title="Cuban cuisine">Cuban</a></li>
# <li><a href="/wiki/Cypriot_cuisine" title="Cypriot cuisine">Cypriot</a></li>
# <li><a href="/wiki/Czech_cuisine" title="Czech cuisine">Czech</a></li>
# <li><a href="/wiki/Danish_cuisine" title="Danish cuisine">Danish</a>
# <ul><li><a href="/wiki/Faroese_cuisine" title="Faroese cuisine">Faroese</a></li>
# <li><a href="/wiki/Greenlandic_cuisine" title="Greenlandic cuisine">Greenlandic</a></li></ul></li>
# <li><a href="/wiki/Djiboutian_cuisine" title="Djiboutian cuisine">Djiboutian</a></li>
# <li><a href="/wiki/Dominica_cuisine" title="Dominica cuisine">Dominican</a></li>
# <li><a href="/wiki/Dominican_Republic_cuisine" title="Dominican Republic cuisine">Dominican Republic</a></li>
# <li><a href="/wiki/Dutch_cuisine" title="Dutch cuisine">Dutch</a></li>
# <li><a href="/wiki/Cuisine_of_East_Timor" title="Cuisine of East Timor">East Timorese</a></li>
# <li><a href="/wiki/Ecuadorian_cuisine" title="Ecuadorian cuisine">Ecuadorian</a></li>
# <li><a href="/wiki/Egyptian_cuisine" title="Egyptian cuisine">Egyptian</a></li>
# <li><a href="/wiki/Emirati_cuisine" title="Emirati cuisine">Emirati</a></li>
# <li><a href="/wiki/Cuisine_of_Equatorial_Guinea" title="Cuisine of Equatorial Guinea">Equatorial Guinean</a></li>
# <li><a href="/wiki/Eritrean_cuisine" title="Eritrean cuisine">Eritrean</a></li>
# <li><a href="/wiki/Estonian_cuisine" title="Estonian cuisine">Estonian</a></li>
# <li><a href="/wiki/Ethiopian_cuisine" title="Ethiopian cuisine">Ethiopian</a></li>
# <li><a href="/wiki/Fijian_cuisine" title="Fijian cuisine">Fijian</a></li>
# <li><a href="/wiki/Filipino_cuisine" title="Filipino cuisine">Filipino</a></li>
# <li><a href="/wiki/Finnish_cuisine" title="Finnish cuisine">Finnish</a></li>
# <li><a href="/wiki/French_cuisine" title="French cuisine">French</a>
# <ul><li><a href="/wiki/Occitan_cuisine" title="Occitan cuisine">Occitan</a></li></ul></li>
# <li><a href="/wiki/Gabonese_cuisine" title="Gabonese cuisine">Gabonese</a></li>
# <li><a href="/wiki/Gambian_cuisine" title="Gambian cuisine">Gambian</a></li>
# <li><a href="/wiki/Georgian_cuisine" title="Georgian cuisine">Georgian</a></li>
# <li><a href="/wiki/German_cuisine" title="German cuisine">German</a></li>
# <li><a href="/wiki/Ghanaian_cuisine" title="Ghanaian cuisine">Ghanaian</a></li>
# <li><a href="/wiki/Greek_cuisine" title="Greek cuisine">Greek</a>
# <ul><li><a href="/wiki/Greek_Macedonian_cuisine" title="Greek Macedonian cuisine">Greek Macedonian</a></li>
# <li><a href="/wiki/Cretan_cuisine" title="Cretan cuisine">Cretan</a></li>
# <li><a href="/wiki/Epirotic_cuisine" title="Epirotic cuisine">Epirotic</a></li>
# <li><a href="/wiki/Cuisine_of_the_Ionian_Islands" title="Cuisine of the Ionian Islands">Heptanesean</a></li></ul></li>
# <li><a href="/wiki/Guatemalan_cuisine" title="Guatemalan cuisine">Guatemalan</a></li>
# <li><a href="/wiki/Guianan_cuisine" title="Guianan cuisine">Guianan</a></li>
# <li><a href="/wiki/Guinea-Bissauan_cuisine" title="Guinea-Bissauan cuisine">Guinea-Bissauan</a></li>
# <li><a href="/wiki/Cuisine_of_Guinea" title="Cuisine of Guinea">Guinean</a></li>
# <li><a href="/wiki/Haitian_cuisine" title="Haitian cuisine">Haitian</a></li>
# <li><a href="/wiki/Honduran_cuisine" title="Honduran cuisine">Honduran</a></li>
# <li><a href="/wiki/Hungarian_cuisine" title="Hungarian cuisine">Hungarian</a></li>
# <li><a href="/wiki/Icelandic_cuisine" title="Icelandic cuisine">Icelandic</a></li>
# <li><a href="/wiki/Indian_cuisine" title="Indian cuisine">Indian</a>
# <ul><li><a href="/wiki/Arunachalese_cuisine" title="Arunachalese cuisine">Arunachalese</a></li>
# <li><a href="/wiki/Assamese_cuisine" title="Assamese cuisine">Assamese</a></li>
# <li><a href="/wiki/Bihari_cuisine" title="Bihari cuisine">Bihari</a></li>
# <li><a href="/wiki/Goan_cuisine" title="Goan cuisine">Goan</a></li>
# <li><a href="/wiki/Goan_Catholic_cuisine" title="Goan Catholic cuisine">Goan Catholic</a></li>
# <li><a href="/wiki/Gujarati_cuisine" title="Gujarati cuisine">Gujarati</a></li>
# <li><a href="/wiki/Culture_of_Himachal_Pradesh#Cuisine" title="Culture of Himachal Pradesh">Himachal Pradesh</a></li>
# <li><a href="/wiki/Kashmiri_cuisine" title="Kashmiri cuisine">Kashmiri</a></li>
# <li><a href="/wiki/Jharkhandi_cuisine" title="Jharkhandi cuisine">Jharkhandi</a></li>
# <li><a href="/wiki/Cuisine_of_Karnataka" class="mw-redirect" title="Cuisine of Karnataka">Karnataka</a></li>
# <li><a href="/wiki/Cuisine_of_Kerala" class="mw-redirect" title="Cuisine of Kerala">Kerala</a></li>
# <li><a href="/wiki/Maharashtrian_cuisine" title="Maharashtrian cuisine">Maharashtrian</a></li>
# <li><a href="/wiki/Manipuri_cuisine" title="Manipuri cuisine">Manipuri</a></li>
# <li><a href="/wiki/Meghalayan_cuisine" title="Meghalayan cuisine">Meghalayan</a></li>
# <li><a href="/wiki/Mizo_cuisine" title="Mizo cuisine">Mizo</a></li>
# <li><a href="/wiki/Naga_cuisine" title="Naga cuisine">Naga</a></li>
# <li><a href="/wiki/Cuisine_of_Odisha" title="Cuisine of Odisha">Odia</a></li>
# <li><a href="/wiki/Rajasthani_cuisine" title="Rajasthani cuisine">Rajasthani</a></li>
# <li><a href="/wiki/Sikkimese_cuisine" title="Sikkimese cuisine">Sikkimese</a></li>
# <li><a href="/wiki/Tamil_cuisine" title="Tamil cuisine">Tamil</a></li>
# <li><a href="/wiki/Telangana_cuisine" title="Telangana cuisine">Telangana</a></li>
# <li><a href="/wiki/Telugu_cuisine" title="Telugu cuisine">Telugu</a></li></ul></li>
# <li><a href="/wiki/Indonesian_cuisine" title="Indonesian cuisine">Indonesian</a>
# <ul><li><a href="/wiki/Acehnese_cuisine" title="Acehnese cuisine">Acehnese</a></li>
# <li><a href="/wiki/Arab_Indonesian_cuisine" title="Arab Indonesian cuisine">Arab</a></li>
# <li><a href="/wiki/Balinese_cuisine" title="Balinese cuisine">Balinese</a></li>
# <li><a href="/wiki/Banjarese_cuisine" class="mw-redirect" title="Banjarese cuisine">Banjarese</a></li>
# <li><a href="/wiki/Batak_cuisine" title="Batak cuisine">Batak</a></li>
# <li><a href="/wiki/Betawi_cuisine" title="Betawi cuisine">Betawi</a></li>
# <li><a href="/wiki/Chinese_Indonesian_cuisine" title="Chinese Indonesian cuisine">Chinese</a></li>
# <li><a href="/wiki/Indian_Indonesian_cuisine" title="Indian Indonesian cuisine">Indian</a></li>
# <li><a href="/wiki/Indo_cuisine" title="Indo cuisine">Indo</a></li>
# <li><a href="/wiki/Javanese_cuisine" title="Javanese cuisine">Javanese</a></li>
# <li><a href="/wiki/Madurese_cuisine" title="Madurese cuisine">Madurese</a></li>
# <li><a href="/wiki/Makassarese_cuisine" class="mw-redirect" title="Makassarese cuisine">Makassarese</a></li>
# <li><a href="/wiki/Minahasan_cuisine" title="Minahasan cuisine">Minahasan</a></li>
# <li><a href="/wiki/Padang_cuisine" title="Padang cuisine">Minangkabau</a></li>
# <li><a href="/wiki/Palembang_cuisine" title="Palembang cuisine">Palembangese</a></li>
# <li><a href="/wiki/Sundanese_cuisine" title="Sundanese cuisine">Sundanese</a></li></ul></li>
# <li><a href="/wiki/Iranian_cuisine" title="Iranian cuisine">Iranian</a></li>
# <li><a href="/wiki/Iraqi_cuisine" title="Iraqi cuisine">Iraqi</a></li>
# <li><a href="/wiki/Irish_cuisine" title="Irish cuisine">Irish</a></li>
# <li><a href="/wiki/Israeli_cuisine" title="Israeli cuisine">Israeli</a></li>
# <li><a href="/wiki/Italian_cuisine" title="Italian cuisine">Italian</a>
# <ul><li><a href="/wiki/Cuisine_of_Abruzzo" title="Cuisine of Abruzzo">Abruzzese</a></li>
# <li><a href="/wiki/Lombard_cuisine" title="Lombard cuisine">Lombard</a></li>
# <li><a href="/wiki/Neapolitan_cuisine" title="Neapolitan cuisine">Neapolitan</a></li>
# <li><a href="/wiki/Roman_cuisine" title="Roman cuisine">Roman</a></li>
# <li><a href="/wiki/Cuisine_of_Sardinia" title="Cuisine of Sardinia">Sardinian</a></li>
# <li><a href="/wiki/Sicilian_cuisine" title="Sicilian cuisine">Sicilian</a></li>
# <li><a href="/wiki/Venetian_cuisine" title="Venetian cuisine">Venetian</a></li></ul></li>
# <li><a href="/wiki/Ivorian_cuisine" title="Ivorian cuisine">Ivorian</a></li>
# <li><a href="/wiki/Jamaican_cuisine" title="Jamaican cuisine">Jamaican</a></li>
# <li><a href="/wiki/Japanese_cuisine" title="Japanese cuisine">Japanese</a>
# <ul><li><a href="/wiki/Okinawan_cuisine" title="Okinawan cuisine">Okinawan</a></li></ul></li>
# <li><a href="/wiki/Jordanian_cuisine" title="Jordanian cuisine">Jordanian</a></li>
# <li><a href="/wiki/Kazakh_cuisine" title="Kazakh cuisine">Kazakh</a></li>
# <li><a href="/wiki/Kenyan_cuisine" class="mw-redirect" title="Kenyan cuisine">Kenyan</a></li>
# <li><a href="/wiki/Korean_cuisine" title="Korean cuisine">Korean</a>
# <ul><li><a href="/wiki/North_Korean_cuisine" title="North Korean cuisine">North Korean</a></li>
# <li><a href="/wiki/South_Korean_cuisine" title="South Korean cuisine">South Korean</a></li></ul></li>
# <li><a href="/wiki/Kosovan_cuisine" title="Kosovan cuisine">Kosovan</a></li>
# <li><a href="/wiki/Kuwaiti_cuisine" title="Kuwaiti cuisine">Kuwaiti</a></li>
# <li><a href="/wiki/Kyrgyz_cuisine" title="Kyrgyz cuisine">Kyrgyz</a></li>
# <li><a href="/wiki/Lao_cuisine" title="Lao cuisine">Lao</a></li>
# <li><a href="/wiki/Latvian_cuisine" title="Latvian cuisine">Latvian</a></li>
# <li><a href="/wiki/Lebanese_cuisine" title="Lebanese cuisine">Lebanese</a></li>
# <li><a href="/wiki/Cuisine_of_Lesotho" title="Cuisine of Lesotho">Lesotho</a></li>
# <li><a href="/wiki/Liberian_cuisine" title="Liberian cuisine">Liberian</a></li>
# <li><a href="/wiki/Libyan_cuisine" title="Libyan cuisine">Libyan</a></li>
# <li><a href="/wiki/Liechtenstein_cuisine" title="Liechtenstein cuisine">Liechtensteiner</a></li>
# <li><a href="/wiki/Lithuanian_cuisine" title="Lithuanian cuisine">Lithuanian</a></li>
# <li><a href="/wiki/Luxembourg%27s_cuisine" class="mw-redirect" title="Luxembourg's cuisine">Luxembourg</a></li>
# <li><a href="/wiki/Macedonian_cuisine" title="Macedonian cuisine">Macedonian</a></li>
# <li><a href="/wiki/Malagasy_cuisine" title="Malagasy cuisine">Malagasy</a></li>
# <li><a href="/wiki/Malawian_cuisine" title="Malawian cuisine">Malawian</a></li>
# <li><a href="/wiki/Malaysian_cuisine" title="Malaysian cuisine">Malaysian</a>
# <ul><li><a href="/wiki/Malaysian_Chinese_cuisine" title="Malaysian Chinese cuisine">Chinese</a></li>
# <li><a href="/wiki/Eurasian_cuisine_of_Singapore_and_Malaysia" title="Eurasian cuisine of Singapore and Malaysia">Eurasian</a></li>
# <li><a href="/wiki/Malaysian_Indian_cuisine" title="Malaysian Indian cuisine">Indian</a></li>
# <li><a href="/wiki/Sabahan_cuisine" title="Sabahan cuisine">Sabahan</a></li>
# <li><a href="/wiki/Sarawakian_cuisine" title="Sarawakian cuisine">Sarawakian</a></li></ul></li>
# <li><a href="/wiki/Maldivian_cuisine" title="Maldivian cuisine">Maldivian</a></li>
# <li><a href="/wiki/Malian_cuisine" title="Malian cuisine">Malian</a></li>
# <li><a href="/wiki/Maltese_cuisine" title="Maltese cuisine">Maltese</a></li>
# <li><a href="/wiki/Mauritanian_cuisine" title="Mauritanian cuisine">Mauritanian</a></li>
# <li><a href="/wiki/Cuisine_of_Mauritius" class="mw-redirect" title="Cuisine of Mauritius">Mauritian</a></li>
# <li><a href="/wiki/Mexican_cuisine" title="Mexican cuisine">Mexican</a></li>
# <li><a href="/wiki/Moldovan_cuisine" title="Moldovan cuisine">Moldovan</a></li>
# <li><a href="/wiki/Mon%C3%A9gasque_cuisine" title="Monégasque cuisine">Monégasque</a></li>
# <li><a href="/wiki/Mongolian_cuisine" title="Mongolian cuisine">Mongolian</a></li>
# <li><a href="/wiki/Montenegrin_cuisine" title="Montenegrin cuisine">Montenegrin</a></li>
# <li><a href="/wiki/Moroccan_cuisine" title="Moroccan cuisine">Moroccan</a></li>
# <li><a href="/wiki/Cuisine_of_Mozambique" class="mw-redirect" title="Cuisine of Mozambique">Mozambican</a></li>
# <li><a href="/wiki/Namibian_cuisine" title="Namibian cuisine">Namibian</a></li>
# <li><a href="/wiki/Cuisine_of_Nauru" class="mw-redirect" title="Cuisine of Nauru">Nauruan</a></li>
# <li><a href="/wiki/Nepalese_cuisine" title="Nepalese cuisine">Nepalese</a></li>
# <li><a href="/wiki/New_Zealand_cuisine" title="New Zealand cuisine">New Zealand</a></li>
# <li><a href="/wiki/Nicaraguan_cuisine" title="Nicaraguan cuisine">Nicaraguan</a></li>
# <li><a href="/wiki/Cuisine_of_Niger" title="Cuisine of Niger">Niger</a></li>
# <li><a href="/wiki/Nigerian_cuisine" title="Nigerian cuisine">Nigerian</a></li>
# <li><a href="/wiki/Niuean_cuisine" title="Niuean cuisine">Niuean</a></li>
# <li><a href="/wiki/Norwegian_cuisine" title="Norwegian cuisine">Norwegian</a></li>
# <li><a href="/wiki/Omani_cuisine" title="Omani cuisine">Omani</a></li>
# <li><a href="/wiki/Pakistani_cuisine" title="Pakistani cuisine">Pakistani</a>
# <ul><li><a href="/wiki/Sindhi_cuisine" title="Sindhi cuisine">Sindhi</a></li></ul></li>
# <li><a href="/wiki/Palestinian_cuisine" title="Palestinian cuisine">Palestinian</a></li>
# <li><a href="/wiki/Panamanian_cuisine" title="Panamanian cuisine">Panamanian</a></li>
# <li><a href="/wiki/Peruvian_cuisine" title="Peruvian cuisine">Peruvian</a>
# <ul><li><a href="/wiki/Chifa" title="Chifa">Chinese</a></li></ul></li>
# <li><a href="/wiki/Polish_cuisine" title="Polish cuisine">Polish</a></li>
# <li><a href="/wiki/Portuguese_cuisine" title="Portuguese cuisine">Portuguese</a></li>
# <li><a href="/wiki/Qatari_cuisine" title="Qatari cuisine">Qatari</a></li>
# <li><a href="/wiki/Romanian_cuisine" title="Romanian cuisine">Romanian</a></li>
# <li><a href="/wiki/Russian_cuisine" title="Russian cuisine">Russian</a>
# <ul><li><a href="/wiki/Bashkir_cuisine" title="Bashkir cuisine">Bashkir</a></li>
# <li><a href="/wiki/Chechen_cuisine" title="Chechen cuisine">Chechen</a></li>
# <li><a href="/wiki/Circassian_cuisine" title="Circassian cuisine">Circassian</a></li>
# <li><a href="/wiki/Komi_cuisine" title="Komi cuisine">Komi</a></li>
# <li><a href="/wiki/Mordovian_cuisine" title="Mordovian cuisine">Mordovian</a></li>
# <li><a href="/wiki/Sakha_cuisine" title="Sakha cuisine">Sakha</a></li>
# <li><a href="/wiki/Tatar_cuisine" title="Tatar cuisine">Tatar</a></li>
# <li><a href="/wiki/Udmurt_cuisine" title="Udmurt cuisine">Udmurt</a></li>
# <li><a href="/wiki/Yamal_cuisine" title="Yamal cuisine">Yamal</a></li></ul></li>
# <li><a href="/wiki/Rwandan_cuisine" title="Rwandan cuisine">Rwandan</a></li>
# <li><a href="/wiki/Cuisine_of_Saint_Helena" title="Cuisine of Saint Helena">Saint Helena</a></li>
# <li><a href="/wiki/Saint_Lucian_cuisine" title="Saint Lucian cuisine">Saint Lucian</a></li>
# <li><a href="/wiki/Salvadoran_cuisine" title="Salvadoran cuisine">Salvadoran</a></li>
# <li><a href="/wiki/Sammarinese_cuisine" title="Sammarinese cuisine">Sammarinese</a></li>
# <li><a href="/wiki/Cuisine_of_S%C3%A3o_Tom%C3%A9_and_Pr%C3%ADncipe" title="Cuisine of São Tomé and Príncipe">São Tomé and Príncipe</a></li>
# <li><a href="/wiki/Saudi_Arabian_cuisine" title="Saudi Arabian cuisine">Saudi Arabian</a></li>
# <li><a href="/wiki/Senegalese_cuisine" title="Senegalese cuisine">Senegalese</a></li>
# <li><a href="/wiki/Serbian_cuisine" title="Serbian cuisine">Serbian</a></li>
# <li><a href="/wiki/Seychellois_cuisine" title="Seychellois cuisine">Seychellois</a></li>
# <li><a href="/wiki/Sierra_Leonean_cuisine" title="Sierra Leonean cuisine">Sierra Leonean</a></li>
# <li><a href="/wiki/Singaporean_cuisine" title="Singaporean cuisine">Singaporean</a></li>
# <li><a href="/wiki/Slovak_cuisine" title="Slovak cuisine">Slovak</a></li>
# <li><a href="/wiki/Slovenian_cuisine" title="Slovenian cuisine">Slovenian</a></li>
# <li><a href="/wiki/Somali_cuisine" title="Somali cuisine">Somali</a></li>
# <li><a href="/wiki/South_African_cuisine" title="South African cuisine">South African</a></li>
# <li><a href="/wiki/Spanish_cuisine" title="Spanish cuisine">Spanish</a>
# <ul><li><a href="/wiki/Andalusian_cuisine" title="Andalusian cuisine">Andalusian</a></li>
# <li><a href="/wiki/Asturian_cuisine" title="Asturian cuisine">Asturian</a></li>
# <li><a href="/wiki/Balearic_cuisine" title="Balearic cuisine">Balearic</a></li>
# <li><a href="/wiki/Basque_cuisine" title="Basque cuisine">Basque</a></li>
# <li><a href="/wiki/Canarian_cuisine" title="Canarian cuisine">Canarian</a></li>
# <li><a href="/wiki/Cantabrian_cuisine" title="Cantabrian cuisine">Cantabrian</a></li>
# <li><a href="/wiki/Catalan_cuisine" title="Catalan cuisine">Catalan</a></li>
# <li><a href="/wiki/Extremaduran_cuisine" title="Extremaduran cuisine">Extremaduran</a></li>
# <li><a href="/wiki/Galician_cuisine" title="Galician cuisine">Galician</a></li>
# <li><a href="/wiki/Manchego_cuisine" title="Manchego cuisine">Manchegan</a></li>
# <li><a href="/wiki/Valencian_cuisine" title="Valencian cuisine">Valencian</a></li></ul></li>
# <li><a href="/wiki/Sri_Lankan_cuisine" title="Sri Lankan cuisine">Sri Lankan</a></li>
# <li><a href="/wiki/Sudanese_cuisine" title="Sudanese cuisine">Sudanese</a></li>
# <li><a href="/wiki/Cuisine_of_Eswatini" title="Cuisine of Eswatini">Swazi</a></li>
# <li><a href="/wiki/Swedish_cuisine" title="Swedish cuisine">Swedish</a></li>
# <li><a href="/wiki/Swiss_cuisine" title="Swiss cuisine">Swiss</a></li>
# <li><a href="/wiki/Syrian_cuisine" title="Syrian cuisine">Syrian</a></li>
# <li><a href="/wiki/Taiwanese_cuisine" title="Taiwanese cuisine">Taiwanese</a></li>
# <li><a href="/wiki/Tajik_cuisine" title="Tajik cuisine">Tajik</a></li>
# <li><a href="/wiki/Tanzanian_cuisine" class="mw-redirect" title="Tanzanian cuisine">Tanzanian</a>
# <ul><li><a href="/wiki/Zanzibari_cuisine" title="Zanzibari cuisine">Zanzibari</a></li></ul></li>
# <li><a href="/wiki/Thai_cuisine" title="Thai cuisine">Thai</a></li>
# <li><a href="/wiki/Togolese_cuisine" title="Togolese cuisine">Togolese</a></li>
# <li><a href="/wiki/Tunisian_cuisine" title="Tunisian cuisine">Tunisian</a></li>
# <li><a href="/wiki/Turkish_cuisine" title="Turkish cuisine">Turkish</a></li>
# <li><a href="/wiki/Trinidad_and_Tobago_cuisine" title="Trinidad and Tobago cuisine">Trinidadian and Tobagonian</a></li>
# <li><a href="/wiki/Ugandan_cuisine" title="Ugandan cuisine">Ugandan</a></li>
# <li><a href="/wiki/Ukrainian_cuisine" title="Ukrainian cuisine">Ukrainian</a></li>
# <li><a href="/wiki/Uruguayan_cuisine" title="Uruguayan cuisine">Uruguayan</a></li>
# <li><a href="/wiki/Uzbek_cuisine" title="Uzbek cuisine">Uzbek</a></li>
# <li><a href="/wiki/Venezuelan_cuisine" title="Venezuelan cuisine">Venezuelan</a></li>
# <li><a href="/wiki/Vietnamese_cuisine" title="Vietnamese cuisine">Vietnamese</a></li>
# <li><a href="/wiki/Western_Saharan_cuisine" title="Western Saharan cuisine">Western Saharan</a></li>
# <li><a href="/wiki/Yemeni_cuisine" title="Yemeni cuisine">Yemeni</a></li>
# <li><a href="/wiki/Zambian_cuisine" title="Zambian cuisine">Zambian</a></li>
# <li><a href="/wiki/Zimbabwean_cuisine" class="mw-redirect" title="Zimbabwean cuisine">Zimbabwean</a></li></ul>
# <ul><li><a href="/wiki/Ainu_cuisine" title="Ainu cuisine">Ainu</a></li>
# <li><a href="/wiki/Anglo-Indian_cuisine" title="Anglo-Indian cuisine">Anglo-Indian</a></li>
# <li><a href="/wiki/Arab_cuisine" title="Arab cuisine">Arab</a></li>
# <li><a href="/wiki/Assyrian_cuisine" title="Assyrian cuisine">Assyrian</a></li>
# <li><a href="/wiki/Balochi_cuisine" title="Balochi cuisine">Balochi</a></li>
# <li><a href="/wiki/Bengali_cuisine" title="Bengali cuisine">Bengali</a></li>
# <li><a href="/wiki/Berber_cuisine" title="Berber cuisine">Berber</a></li>
# <li><a href="/wiki/Buddhist_cuisine" title="Buddhist cuisine">Buddhist</a></li>
# <li><a href="/wiki/Cajun_cuisine" title="Cajun cuisine">Cajun</a></li>
# <li><a href="/wiki/Christian_dietary_laws" title="Christian dietary laws">Christian</a></li>
# <li><a href="/wiki/Crimean_Tatar_cuisine" title="Crimean Tatar cuisine">Crimean Tatar</a></li>
# <li><a href="/wiki/Hazaragi_cuisine" title="Hazaragi cuisine">Hazaragi</a></li>
# <li><a href="/wiki/Diet_in_Hinduism" title="Diet in Hinduism">Hindu</a></li>
# <li><a href="/wiki/Inuit_cuisine" title="Inuit cuisine">Inuit</a></li>
# <li><a href="/wiki/Islamic_dietary_laws" title="Islamic dietary laws">Islamic</a></li>
# <li><a href="/wiki/Jain_vegetarianism" title="Jain vegetarianism">Jain</a></li>
# <li><a href="/wiki/Jewish_cuisine" title="Jewish cuisine">Jewish</a>
# <ul><li><a href="/wiki/American_Jewish_cuisine" title="American Jewish cuisine">American</a></li>
# <li><a href="/wiki/Ashkenazi_Jewish_cuisine" title="Ashkenazi Jewish cuisine">Ashkenazi</a></li>
# <li><a href="/wiki/Bukharan_Jewish_cuisine" title="Bukharan Jewish cuisine">Bukharan</a></li>
# <li><a href="/wiki/Ethiopian_Jewish_cuisine" title="Ethiopian Jewish cuisine">Ethiopian</a></li>
# <li><a href="/wiki/Mizrahi_Jewish_cuisine" title="Mizrahi Jewish cuisine">Mizrahi</a></li>
# <li><a href="/wiki/Sephardic_Jewish_cuisine" title="Sephardic Jewish cuisine">Sephardic</a></li>
# <li><a href="/wiki/Syrian_Jewish_cuisine" title="Syrian Jewish cuisine">Syrian</a></li></ul></li>
# <li><a href="/wiki/Kurdish_cuisine" title="Kurdish cuisine">Kurdish</a></li>
# <li><a href="/wiki/Livonian_cuisine" title="Livonian cuisine">Livonian</a></li>
# <li><a href="/wiki/Malay_cuisine" title="Malay cuisine">Malay</a></li>
# <li><a href="/wiki/Mennonite_cuisine" title="Mennonite cuisine">Mennonite</a></li>
# <li><a href="/wiki/Indigenous_cuisine_of_the_Americas" title="Indigenous cuisine of the Americas">Indigenous American</a></li>
# <li><a href="/wiki/Parsi_cuisine" title="Parsi cuisine">Parsi</a></li>
# <li><a href="/wiki/Pashtun_cuisine" title="Pashtun cuisine">Pashtun</a></li>
# <li><a href="/wiki/Peranakan_cuisine" title="Peranakan cuisine">Peranakan</a></li>
# <li><a href="/wiki/Punjabi_cuisine" title="Punjabi cuisine">Punjabi</a></li>
# <li><a href="/wiki/Romani_cuisine" title="Romani cuisine">Romani</a></li>
# <li><a href="/wiki/Sami_cuisine" class="mw-redirect" title="Sami cuisine">Sami</a></li>
# <li><a href="/wiki/Diet_in_Sikhism" title="Diet in Sikhism">Sikh</a></li>
# <li><a href="/wiki/Yup%27ik_cuisine" title="Yup'ik cuisine">Yup'ik</a></li></ul>
# <ul><li><a href="/wiki/Ancient_Egyptian_cuisine" title="Ancient Egyptian cuisine">Ancient Egyptian</a></li>
# <li><a href="/wiki/Ancient_Greek_cuisine" title="Ancient Greek cuisine">Ancient Greek</a></li>
# <li><a href="/wiki/Ancient_Israelite_cuisine" title="Ancient Israelite cuisine">Ancient Israelite</a></li>
# <li><a href="/wiki/Ancient_Roman_cuisine" title="Ancient Roman cuisine">Ancient Roman</a></li>
# <li><a href="/wiki/Aztec_cuisine" title="Aztec cuisine">Aztec</a></li>
# <li><a href="/wiki/Byzantine_cuisine" title="Byzantine cuisine">Byzantine</a></li>
# <li><a href="/wiki/Early_modern_European_cuisine" title="Early modern European cuisine">Early modern European</a></li>
# <li><a href="/wiki/History_of_Chinese_cuisine" title="History of Chinese cuisine">Historical Chinese</a></li>
# <li><a href="/wiki/History_of_Indian_cuisine" title="History of Indian cuisine">Historical Indian subcontinent</a></li>
# <li><a href="/wiki/History_of_seafood" title="History of seafood">History of seafood</a></li>
# <li><a href="/wiki/History_of_vegetarianism" title="History of vegetarianism">History of vegetarianism</a></li>
# <li><a href="/wiki/Inca_cuisine" title="Inca cuisine">Inca</a></li>
# <li><a href="/wiki/Maya_cuisine" class="mw-redirect" title="Maya cuisine">Mayan</a></li>
# <li><a href="/wiki/Medieval_cuisine" title="Medieval cuisine">Medieval</a></li>
# <li><a href="/wiki/Ottoman_cuisine" title="Ottoman cuisine">Ottoman</a></li>
# <li><a href="/wiki/Peasant_foods" title="Peasant foods">Peasant</a></li>
# <li><a href="/wiki/Soviet_cuisine" title="Soviet cuisine">Soviet</a></li>
# <li><a href="/wiki/Cuisine_of_the_Thirteen_Colonies" title="Cuisine of the Thirteen Colonies">Thirteen Colonies</a></li></ul>
# <ul><li><a href="/wiki/Cuisine_classique" class="mw-redirect" title="Cuisine classique">Classique</a></li>
# <li><a href="/wiki/Fast_food" title="Fast food">Fast food</a></li>
# <li><a href="/wiki/Fusion_cuisine" title="Fusion cuisine">Fusion</a></li>
# <li><a href="/wiki/Haute_cuisine" title="Haute cuisine">Haute</a></li>
# <li><a href="/wiki/Molecular_gastronomy" title="Molecular gastronomy">Molecular gastronomy</a></li>
# <li><a href="/wiki/Note_by_Note_cuisine" title="Note by Note cuisine">Note by Note</a></li>
# <li><a href="/wiki/Nouvelle_cuisine" title="Nouvelle cuisine">Nouvelle</a></li></ul>
#   '''
#   soup = bs(cuisineHTMLData, 'lxml')
#   cuisineList = soup.findAll('li' )
#   cuisineCollection = []
#   for cuisine in cuisineList:
#     if cuisine.text.find('\n') != -1:
#       # print('skip: ' + cuisine.text)
#       # print(cuisine.text.split("\n"))
#       cuisineMulti = cuisine.text.split("\n")
#       for cui in cuisineMulti:
#         cuisineCollection.append(('\'' + cui + '\',').lower())

#       continue
#     # print('\'' + cuisine.text + '\'')
#     cuisineCollection.append(('\'' + cuisine.text + '\',').lower())

#   # cuisineSet = list(dict.fromkeys(cuisineCollection))
#   cuisineSet = list(set(cuisineCollection))
#   sortedCuisine = sorted(cuisineSet)

#   for cuisine in sortedCuisine:
#     print(cuisine)

# a = parser.parse(" August 6, 2021")
# scrap()
