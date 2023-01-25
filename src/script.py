import importlib
import os
import requests
from bs4 import BeautifulSoup
from importlib import util as importlib_util
import sys

# from .. import YamlCleanup

# from utils.utils import YamlCleanup
from utils.utils import YamlCleanup
from assets.service_properties import service_details, service_list


# import importlib
# YamlCleanup = importlib.import_module(os.path.normpath(os.path.join(__file__,'../../', 'utils','utils.py'))).YamlCleanup



class Service:
    def __init__(self, name, url, subservices=None):
        self.name = name
        self.url = url
        self.subservices = subservices

    def set_subservices(self, subservices):
        self.subservices = subservices


class SubService:

    def __init__(self, name, url, properties=None):
        self.name = name
        self.url = url
        self.properties = properties

    def set_properties(self, properties):
        self.properties = properties


class WebScraper:
    main_html_tag = 'div'
    main_html_class = 'highlights'
    main_url = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html"
    service_html_tag = 'ul'
    service_html_class = "itemizedlist"
    property_html_tag = 'div'
    property_html_id = "YAML"
    file_path = os.path.normpath(os.path.join(__file__, '../../', 'assets', 'service_properties.py'))

    def __init__(self, home_url=None, services=None):
        self.home_url = home_url if home_url else self.main_url
        self.services = services if services else {}
        self.existing_services = {}
        # modify_and_import('get_service_details', 'assets.service_properties', lambda x: True)
        # self.existing_service_list = []

        self.read_from_file()
        # self.service_objects = {}

    def get_soup_object(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def read_from_file(self):
        # print(service_details)
        # print(type(service_details))
        for service in service_details:
            # subservices = service['subservices']
            # print(service)
            # print(type(service))
            subservices_list = []
            for subservice in service_details[service]['subservices']:
                print(subservice)
                name = service_details[service]['subservices'][subservice]['name']
                url = service_details[service]['subservices'][subservice]['url']
                properties = service_details[service]['subservices'][subservice]['properties']
                subservices_list.append(
                    SubService(
                        name=name,
                        url=url,
                        properties=properties
                    )
                )

            self.existing_services[service] = Service(service,
                                                      service_details[service]['url'],
                                                      subservices_list)

    def get_service(self, service_name):
        if self.existing_services:
            self.services[service_name] = self.existing_services[service_name]

        else:
            soup = self.get_soup_object(WebScraper.main_url)
            aws_service_elements = soup.find_all(WebScraper.main_html_tag,
                                                 class_=WebScraper.main_html_class,
                                                 )

            for element in aws_service_elements:
                for li in element.ul:
                    if li.a.text == service_name:
                        self.services[li.a.text] = Service(li.a.text, li.a['href'])
                        if li.a.text not in service_list:
                            service_list.append(li.a.text)

            print(self.services)
                    # return Service(li.a.text, li.a['href'])
            # url = WebScraper.main_url.rsplit("/", 1)[0] + "/" + self.serv


    def get_services(self):
        if not self.services:
            soup = self.get_soup_object(WebScraper.main_url)
            aws_service_elements = soup.find_all(
                WebScraper.main_html_tag, class_=WebScraper.main_html_class)
            for element in aws_service_elements:
                print(element)
                for li in element.ul:
                    print(li.a.text)
                    self.services[li.a.text] = Service(li.a.text, li.a['href'])

                    # self.services.append(Service(li.a.text, li.a.get('href')))

        # for service in self.services:
        # self.service_objects[service[0]] = Service(service[0], service[1])

    def get_subservices(self, service_name):
        # print(self.services)
        url = WebScraper.main_url.rsplit(
            "/", 1)[0] + "/" + self.services[service_name].url.split("./")[1]
        soup = self.get_soup_object(url)
        subservice_elements = soup.find_all(
            WebScraper.service_html_tag, class_=WebScraper.service_html_class)
        subservice_list = []
        for element in subservice_elements:
            for li in element:
                subservice_list.append(SubService(li.a.text, li.a.get('href')))
        self.services[service_name].set_subservices(subservice_list)

    def get_properties(self, service_name, sub_service_name):
        url = WebScraper.main_url.rsplit(
            "/", 1)[0] + "/" + self.services[service_name][sub_service_name].url.split("./")[1]
        soup = self.get_soup_object(url)
        property_elements = soup.find(
            WebScraper.property_html_tag, id=WebScraper.property_html_id)
        code_elem = property_elements.pre.code
        props = YamlCleanup(str(code_elem)).get_props()
        self.services[service_name][sub_service_name].properties = props

    def write_to_file(self):
        service_details = {}
        for service in self.services.keys():
            # print(service, type(service))
            name = self.services[service].name
            url = self.services[service].url
            subservices = self.services[service].subservices
            service_details[name] = {'name': name, 'url': url, 'subservices': {}}
            subservice_dict = {}
            if subservices:
                for i in subservices:
                    subservice_dict[i.name] = {'name': i.name, 'url': i.url, 'properties': i.properties}
            service_details[name]['subservices'] = subservice_dict
            print(service_details)

        with open(WebScraper.file_path, 'w') as f:
            f.write(f"service_details = {service_details}")
            f.write(f"service_list = {service_list}")


            # self.existing_services[service] =

# aws_url = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html"
# aws_page = requests.get(aws_url)

# aws_soup = BeautifulSoup(aws_page.content, "html.parser")

# aws_service_elements = aws_soup.find_all("div", class_="highlights")


# aws_service_list = []

# for element in aws_service_elements:
#     # print(element.prettify(), end="\n"*2)
#     for li in element.ul:
#         aws_service_list.append((li.a.text, li.a.get('href')))

#     # break

# print(aws_service_list)

# aws_sub_service_list = []
# aws_service_sub_service_mapping = {}
# for service in aws_service_list:
#     aws_service_sub_service_mapping[service[0]] = []
#     service_main_page_url = aws_url.rsplit(
#         "/", 1)[0] + '/' + service[1].split("./")[1]
#     # print(service_main_page_url)
#     service_main_page = requests.get(service_main_page_url)
#     service_main_soup = BeautifulSoup(service_main_page.content, "html.parser")
#     service_resource_type_elements = service_main_soup.find_all(
#         "ul", class_="itemizedlist")
#     for element in service_resource_type_elements:
#         # print(element.prettify(), end="\n"*2)
#         for li in element:
#             aws_sub_service_list.append((li.a.text, li.a.get('href')))
#             aws_service_sub_service_mapping[service[0]].append(li.a.text)

#     # print(aws_sub_service_list)
#     # print(len(aws_sub_service_list))
#     # break
# print(aws_sub_service_list)
# print(aws_service_sub_service_mapping)

# # service_to_subservice_list = list(zip(aws_service_list))
# #
# # service_to_subservice_mapping = {k:v in }
# sub_service_property_mapping = {}
# for service in aws_sub_service_list:
#     sub_service_page_url = aws_url.rsplit(
#         "/", 1)[0] + '/' + service[1].split("./")[1]
#     sub_service_page = requests.get(sub_service_page_url)
#     sub_service_soup = BeautifulSoup(sub_service_page.content, "html.parser")
#     sub_service_yaml_elements = sub_service_soup.find("div", id='YAML')
#     code_elem = sub_service_yaml_elements.pre.code
#     props = YamlCleanup(str(code_elem)).get_props()
#     sub_service_property_mapping[service[0]] = props
#     # break

# # print(aws_service_list)

# print(sub_service_property_mapping)
