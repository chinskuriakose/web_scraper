# import pickle
# from datetime import datetime
# from time import perf_counter
# import requests
# import requests
# from bs4 import BeautifulSoup as bs
# from lxml import html
#
# # from utils import connect, get_cookies, get_meta
#
# def get_data(url,xpath):
#     res=requests.get(url)
#     sources_list = html.fromstring(res.text)
#     sources=sources_list.xpath(f'{xpath}/text()')
#     sources_links=sources_list.xpath(f'{xpath}/@href')
#     return list(zip(sources,sources_links))
#
#
# def main():
#     result=get_data('https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html','//*[@id="main-col-body"]/div[2]/ul/li/a')
#     # final_data={}
#     for i in result[:1]:
#         sub_url=f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{i[1][1:]}'
#         sub_xpath='//*[@id="main-col-body"]/div[2]/ul/li/p/a'
#         sub_source_res=get_data(sub_url,sub_xpath)
#         for sub_s in sub_source_res[:1]:
#             yaml_url = (f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{sub_s[1][1:]}')
#             # print(yaml_url)
#             yaml_res=requests.get(f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{sub_s[1][1:]}')
#             yaml_data = html.fromstring(yaml_res.text)
#             # soup = bs(yaml_res.text, 'html5lib')
#             prop_keys=yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
#             prop_values=yaml_data.xpath('//*[@id="YAML"]/pre/code/code/text()')
#             prop_values=[i.strip() for i in prop_values]
#             prop=dict(zip(prop_keys,prop_values))
#             print(prop)
#
#             for i, j in prop.items():
#                 if j=='':
#                     print(i,'----------')
#                     get_yaml_data(i,yaml_data)
#
#
# # def get_yaml_data(i,yaml_data):
# #     prop_keys=yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
# #     urls=yaml_data.xpath(f'//*[@id="YAML"]/pre/code/code[{prop_keys.index(i)+1}]/a/@href')[0]
# #     res1=requests.get(f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{urls[1:]}')
# #     yaml_data = html.fromstring(res1.text)
# #     # print(yaml_data)
# #     prop_keys=yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
# #     prop_v=yaml_data.xpath('//*[@id="YAML"]/pre/code/code/text()')
# #     prop_values=[i.strip() for i in prop_v]
# #     prop=dict(zip(prop_keys,prop_values))
# #     for i , j in prop.items():
# #         if j!='':
# #             return prop
# #         else:
# #             get_yaml_data(i,yaml_data)
#
# def get_yaml_data(i, yaml_data):
#     prop_keys = yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
#     index = prop_keys.index(i) if i in prop_keys else -1
#     if index < 0:
#         return {}
#     urls = yaml_data.xpath(f'//*[@id="YAML"]/pre/code/code[{index+1}]/a/@href')[0]
#     res1 = requests.get(f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{urls[1:]}')
#     yaml_data = html.fromstring(res1.text)
#     prop_keys = yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
#     prop_v = yaml_data.xpath('//*[@id="YAML"]/pre/code/code/text()')
#     prop_values = [i.strip() for i in prop_v]
#     prop = dict(zip(prop_keys, prop_values))
#     for i, j in prop.items():
#         if j != '':
#             return prop
#         else:
#             return get_yaml_data(i, yaml_data)
#
# if __name__ == '__main__':
#     main()

import pickle
from datetime import datetime
from time import perf_counter
import requests
from bs4 import BeautifulSoup as bs
from lxml import html

def get_data(url,xpath):
    res=requests.get(url)
    sources_list = html.fromstring(res.text)
    sources=sources_list.xpath(f'{xpath}/text()')
    sources_links=sources_list.xpath(f'{xpath}/@href')
    return list(zip(sources,sources_links))


def main():
    result = get_data('https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html','//*[@id="main-col-body"]/div[2]/ul/li/a')
    for i in result:
        sub_url = f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{i[1][1:]}'
        # print(sub_url)
        sub_xpath = '//*[@id="main-col-body"]/div[2]/ul/li/p/a'
        sub_source_res = get_data(sub_url, sub_xpath)
        for sub_s in sub_source_res:
            yaml_url = f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{sub_s[1][1:]}'
            yaml_res = requests.get(yaml_url)
            yaml_data = html.fromstring(yaml_res.text)
            prop_keys = yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
            prop_values = yaml_data.xpath('//*[@id="YAML"]/pre/code/code/text()')
            prop_values = [i.strip() for i in prop_values]
            prop = dict(zip(prop_keys, prop_values))
            # print(prop)
            for i, j in prop.items():
                if j == '':
                    print(i, '----------')
                    prop = get_yaml_data(i, yaml_data)
                    print(prop)


def get_yaml_data(i, yaml_data):
    prop_keys = yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
    urls = yaml_data.xpath(f'//*[@id="YAML"]/pre/code/code[{prop_keys.index(i)+1}]/a/@href')[0]
    res1 = requests.get(f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{urls[1:]}')
    yaml_data = html.fromstring(res1.text)
    prop_keys = yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
    prop_v = yaml_data.xpath('//*[@id="YAML"]/pre/code/code/text()')
    prop_values = [i.strip() for i in prop_v]
    prop = dict(zip(prop_keys, prop_values))
    for i, j in prop.items():
        if j != '':
            return prop
        else:
            return get_yaml_data(i, yaml_data)

if __name__ == '__main__':
    main()

# def sub_service(sub_service_name):
#     yaml_url = f'https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide{sub_service_name[1][1:]}'
#     print(yaml_url)
#     # yaml_res = requests.get(yaml_url)
    # yaml_data = html.fromstring(yaml_res.text)
    # prop_keys = yaml_data.xpath('//*[@id="YAML"]/pre/code/a/text()')
    # prop_values = yaml_data.xpath('//*[@id="YAML"]/pre/code/code/text()')
    # prop_values = [i.strip() for i in prop_values]
    # prop = dict(zip(prop_keys, prop_values))
    #

