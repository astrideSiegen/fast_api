import os
import requests


# définition de l'adresse de l'API
api_address = '127.0.0.1' 
# port de l'API
api_port = 8000


#credentials
credentials = [
    {"username":"alice","password": "wonderland"},
    {"username":"bob", "password":"builder"},
    {"username":"clementine", "password":"mandarine"}

]

# requête 
for credential in credentials:
    r = requests.get(
    url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
         params= {
        'username': credential["username"],
        'password': credential["password"],
        }
   )
    
 
    
  # affichage des résultats
    print(f"Testing user {credential['username']} with password {credential['password']}")
    print("response:", r.json())
    # print("Status Code:", r.status_code)
    # print("Response Body:", r.text)

   # # statut de la requête
    status_code = r.status_code
    result = "SUCCESS" if status_code == 200 else "FAILURE"

    output = f"""
    ============================
    Authentication Test
   ============================

  Request to "/permissions"
  | username="{credential['username']}"
  | password="{credential['password']}"

   expected result = 200
   Actual code = {status_code}

   ==> {result}
   """
 

    print(output)


#impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)
        print('Hello Heloo')

#################################################

# output = '''
# ============================
#     Authentication test
# ============================

# request done at "/permissions"
# | username="alice"
# | password="wonderland"

# expected result = 200
# actual restult = {status_code}

# ==>  {test_status}

# '''


# # statut de la requête
# status_code = r.status_code

# # affichage des résultats
# if status_code == 200:
#     test_status = 'SUCCESS'
# else:
#     test_status = 'FAILURE'
# print(output.format(status_code=status_code, test_status=test_status))

# # impression dans un fichier
# if os.environ.get('LOG') == 1:
#     with open('api_test.log', 'a') as file:
#         file.write(output)
