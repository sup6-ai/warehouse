# import requests
# URL = http://127.0.0.1:8000
# user_credentials = {"username":"sup","password":"12345"}

# response = request.post(url=URL+ "/login" ,json=user_credentials)
# print(response.status_code)
# print(response.json())


# response_json = response.json()
# access_token = response_json["access_token"]
# refresh_token = response_json["refresh_token"]


# # registering a package
# header = {"token" : access_token}
# response = request.post(url = URL+ " /register" ,headers=header)
# print(response.status_code)
# print(response.json())

# # adding a package
# header = {"token":access_token}
# response = request.post(url=URL + "/packages" ,headers=header)
# print(response.status_body)
# print(response.json())

# # get package
# header = {"token" : access_token}
# response = request.get(url = URL + "/packages" ,headers=header)
# print(response.status_code)
# print(response.json())

# # get package through package_id
# header = ("token" : access_token)
# response = request.get(url=URL + "/packages/{package_id}",headers=header)
# print(response.status_code)
# print(response.json())

# #update package
# header = ("token" : access_token)
# response = request.patch(url=URL + "/packages/{package_id}",headers=header)
# print(response.status_code)
# print(response.json())

# # delete
# header = ("token" : access_type)
# response = request.delete(url=URL + "/packages/{package_id}",headers=header)
# print(response.status_code)
# print(response.json())

# # view dispatch batches
# header= ("token" : access_token)
# response = request.get(url=URL + "/dispatch-batches",headers=header)
# print(response.status_code)
# print(response.json())

# # add dispatch-batches
# header = {"token" : access_token}
# response = request.post(url=URL + "/dispatch-batches",headers=header)
# print(response.status_code)
# print(response.json)

# # get warehouse
# header = {"token" : access_token}
# response = request.get(url=URL + "/warehouse/statistics",headers=header)
# print(response.status_code)
# print(response.json)


import requests

URL = "http://127.0.0.1:8000"
user_credentials = {"user_name": "sup", "password": "12345"}

# login - 200
response = requests.post(url=URL + "/login", json=user_credentials)
print(response.status_code)
print(response.json())

response_json = response.json()
access_token = response_json["access_token"]
refresh_token = response_json["refresh_token"]

header = {"token": access_token}


# registering a user
new_user = {"user_name": "newuser", "password": "12345"}
response = requests.post(url=URL + "/register", json=new_user)
print(response.status_code)
print(response.json())


# adding a package
package_details = {
    "package_name": "Laptop",
    "destination": "Bangalore",
    "weight": 2.5,
    "arrival_date": "2026-12-12"
}

response = requests.post(url=URL + "/packages", headers=header, json=package_details)
print(response.status_code)
print(response.json())


# get package
response = requests.get(url=URL + "/packages", headers=header)
print(response.status_code)
print(response.json())


# get package through package_id
package_id = 1
response = requests.get(url=URL + f"/packages/{package_id}", headers=header)
print(response.status_code)
print(response.json())


# update package
updated_details = {"destination": "Chennai"}
response = requests.patch(url=URL + f"/packages/{package_id}", headers=header, json=updated_details)
print(response.status_code)
print(response.json())


# delete package
response = requests.delete(url=URL + f"/packages/{package_id}", headers=header)
print(response.status_code)
print(response.json())


# view dispatch batches
response = requests.get(url=URL + "/dispatch-batches", headers=header)
print(response.status_code)
print(response.json())


# add dispatch-batches
dispatch_details = {
    # Enter the required fields from Swagger
}

response = requests.post(url=URL + "/dispatch-batches", headers=header, json=dispatch_details)
print(response.status_code)
print(response.json())


# get warehouse
response = requests.get(url=URL + "/warehouse/statistics", headers=header)
print(response.status_code)
print(response.json())


# refresh token
response = requests.post(url=URL + "/refresh", json={"refresh_token": refresh_token})
print(response.status_code)
print(response.json())
