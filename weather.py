__author__ = 'mwas'

import os
from suds.client import  Client

# path of weather wsdl file
weather_wsdl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Weather.asmx.xml"))

weather_wsdl_url = "file://" + weather_wsdl_path


weather_client = Client(weather_wsdl_url)

# a simple example for one of the methods
print weather_client.service.GetWeatherInformation()


