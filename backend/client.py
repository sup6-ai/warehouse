# # import requests
# # URL = "http://127.0.0.1:8000"
# # user_credentials = {"user_name": "sup", "password": "12345"}

# # response = requests.post(url=URL + "/login", json=user_credentials)
# # print(response.status_code)
# # print(response.text)


# # response_json = response.json()
# # access_token = response_json["access_token"]
# # refresh_token = response_json["refresh_token"]

# # header = {"token": access_token}
# # response = requests.get(url=URL + "/packages", headers=header)
# # print(response.status_code)
# # print(response.json())

# # response = requests.get(url=URL + "/")


# # response = requests.get(url=URL + "/warehouse/statistics", headers=header)
# # print(response.status_code)
# # print(response.json())


# # response = requests.delete(url=URL + "/packages/1", headers=header)
# # print(response.status_code)
# # print(response.json())

# # status = input("Enter status: ")
# # response = requests.post(url=URL+"/dispatch-batches", headers=header, json=status)
# # print(response.status_code)
# # print(response.json())

# # respone=requests.get

# import requests

# URL = "http://127.0.0.1:8000"
# user_credentials = {"user_name": "sup", "password": "12345"}

# # login -200
# response = requests.post(url=URL + "/login", json=user_credentials)
# print(response.status_code)
# print(response.json())

# response_json = response.json()
# access_token = response_json["access_token"]
# refresh_token = response_json["refresh_token"]

# # registering a package-422
# header = {"token": access_token}
# response = requests.post(url=URL + "/register", headers=header)
# print(response.status_code)
# print(response.json())

# # adding a package-422
# response = requests.post(url=URL + "/packages", headers=header)
# print(response.status_code)
# print(response.json())

# # get package-200
# response = requests.get(url=URL + "/packages", headers=header)
# print(response.status_code)
# print(response.json())

# # get package through package_id-200
# package_id = 1
# response = requests.get(url=URL + f"/packages/{package_id}", headers=header)
# print(response.status_code)
# print(response.json())

# # update package-422
# response = requests.patch(url=URL + f"/packages/{package_id}", headers=header)
# print(response.status_code)
# print(response.json())

# # delete-403
# response = requests.delete(url=URL + f"/packages/{package_id}", headers=header)
# print(response.status_code)
# print(response.json())

# # view dispatch batches-200
# response = requests.get(url=URL + "/dispatch-batches", headers=header)
# print(response.status_code)
# print(response.json())

# # add dispatch-batches-422
# response = requests.post(url=URL + "/dispatch-batches", headers=header)
# print(response.status_code)
# print(response.json())

# # get warehouse 403
# response = requests.get(url=URL + "/warehouse/statistics", headers=header)
# print(response.status_code)
# print(response.json())




