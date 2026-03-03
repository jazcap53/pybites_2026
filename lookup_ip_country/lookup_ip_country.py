import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    url_str = IPINFO_URL.format(ip=ip_address)
    geo_data = requests.get(url_str)
    return geo_data.json()['country']



if __name__ == '__main__':
    print(get_ip_country("187.190.38.36"))