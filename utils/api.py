from utils.http_methods import Http_method

""" Методы для тестирования Google maps API"""

BASE_URL = 'https://rahulshettyacademy.com'         #Базовая URL
KEY = '?key=qaclick123'

class Google_maps_api():

    """ Метод для создания новой локации (POST запрос) """
    @staticmethod
    def create_new_place():

        json_create_new_place = {
            "location": {
            "lat": -38.383494,
            "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
             "shoe park",
            "shop"
             ],
             "website": "http://google.com",
            "language": "French-IN"
             }

        post_resource = '/maps/api/place/add/json'      # Ресурс метода POST
        post_url = BASE_URL + post_resource + KEY
        result_post = Http_method.post(post_url,json_create_new_place)
        return result_post

    """ Метод для изменения новой локации"""

    @staticmethod
    def get_new_place(place_id):

        get_resource = "/maps/api/place/get/json"      # Ресурс метода GET
        get_url = BASE_URL + get_resource + KEY + "&place_id=" + place_id
        print(get_url)
        result_get = Http_method.get(get_url)
        print(result_get.json())
        return result_get

    """ Метод для изменения новой локации  """

    @staticmethod
    def put_new_place(place_id):
        get_resource = "/maps/api/place/update/json"  # Ресурс метода PUT
        body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_url = BASE_URL + get_resource + KEY
        result_put = Http_method.put(put_url,body)
        print(result_put.json())
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        get_resource = "/maps/api/place/delete/json"  # Ресурс метода DELETE
        body = {
            "place_id": place_id,
        }
        put_url = BASE_URL + get_resource + KEY
        result_delete = Http_method.put(put_url, body)
        print(result_delete.json())
        return result_delete













