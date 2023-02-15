# import requests
# import json
# from bs4 import BeautifulSoup
#
# url = 'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html'
#
# r = requests.get(url)
#
# soup = BeautifulSoup(r.content, 'html.parser')

from web_scraper.src.script import WebScraper

anny = WebScraper()
anny.read_from_file()
# anny.get_service('AWS Private CA')

# print(anny.get_service(service_name='AWS Private CA'))
# anny.read_from_file()
# anny.get_service(service_name='AWS Private CA')
# anny.get_services()
# anny.get_properties('AWS Private CA','AWS::ACMPCA::Certificate')
# print(anny.read_from_file())
# print(anny.get_soup_object(url='https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html'))
# print(anny.get_properties())
# print(anny.read_from_file())