from script import WebScraper, Service, SubService
import os
if __name__ == "__main__":

    # print(os.getcwd())
    # print(__file__)
    # print(os.path.normpath(os.path.join(__file__, '../../', 'utils', 'utils.py')))


    home_url = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html"

    # Create a WebScraper object
    web_scraper = WebScraper(home_url=home_url)
    web_scraper.get_services()
    print(web_scraper.services)


    # Create a Service object
    # service = Service()

    # Create a SubService object
    # sub_service = SubService()

    # Add the web scraper to the service