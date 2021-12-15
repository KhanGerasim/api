import requests
import json


class PetFriends():
    def get_api_key(self,email: str, passwd: str):
        headers = { 'email': email, 'password': passwd, } 
        res = requests.get('https://petfriends1.herokuapp.com/api/key',  headers=headers) 
        status = res.status_code 
        try: 
            result = res.json() 
        except json.decoder.JSONDecodeError: 
            result = res.text 
        return status, result


    def get_api_pets(self, auth_key: str, filter: str):
        header = {'auth_key': auth_key}
        query = {"filter": filter}
        res = requests.get('https://petfriends1.herokuapp.com/api/pets',  headers=header, data=query)
        status = res.status_code
        try:
            result = res
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def post_api_create_pet_simple(self, auth_key: str, name: str, age: str,animal_type: str):
        header = {'auth_key': auth_key}
        formData = {"name": name, "age": age, "animal_type":animal_type}
        res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple',  headers=header, data=formData)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def post_api_create_pets(self, auth_key: str, name: str, age: str,animal_type: str, pet_photo: str):
        header = {'auth_key': auth_key}
        formData = {"name": name, "age": age, "animal_type": animal_type}
        files = {"pet_photo": pet_photo}
        res = requests.post('https://petfriends1.herokuapp.com/api/pets',  headers=header, data=formData, files=files)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

