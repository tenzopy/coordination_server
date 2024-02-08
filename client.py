
import requests
ALLOWED_HOSTS = ['127.0.0.1','192.168.43.219']

new_data = {
        "host":str(ALLOWED_HOSTS[0]),
    }
url_post = "http://100.73.159.142:8000/"


requests.post(url_post, json=new_data)
