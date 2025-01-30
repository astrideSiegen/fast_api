import os
import requests

# définition de l'adresse de l'API
api_address = 'localhost' 
# port de l'API
api_port = 8000


#credentials
values = [
    {"username":"alice","password": "wonderland","sentence": "Hello world" },
    {"username":"bob", "password":"builder","sentence": "Hello world"}

]

for value in values:
    r = requests.get(
    url='http://{address}:{port}/v1/sentiment'.format(address=api_address, port=api_port),
         params= {
        'username': value["username"],
        'password': value["password"],
        'sentence': value["sentence"]
        }
   )
    
 
    
  # affichage des résultats
    print(f"Testing user {value['username']} with password {value['password']} on Version 1")
    print("response:", r.json())
    # print("Status Code:", r.status_code)
    # print("Response Body:", r.text)

   # # statut de la requête
    status_code = r.status_code
    result = "SUCCESS" if status_code == 200 else "FAILURE"

    output = f"""
    ============================
    Authorization Test Version 1
   ============================

  Request to "/v1/sentiment"
  | username="{value['username']}"
  | password="{value['password']}"
  | sentence="{value['sentence']}"

   expected result = 200
   Actual code = {status_code}

   ==> {result}
   """

    print(output)




for value in values:
    r = requests.get(
    url='http://{address}:{port}/v2/sentiment'.format(address=api_address, port=api_port),
         params= {
        'username': value["username"],
        'password': value["password"],
        'sentence': value["sentence"]
        }
   )
    
 
    
  # affichage des résultats
    print(f"Testing user {value['username']} with password {value['password']} on version 2")
    print("response:", r.json())
    # print("Status Code:", r.status_code)
    # print("Response Body:", r.text)

   # # statut de la requête
    status_code = r.status_code
    result = "SUCCESS" if status_code == 200 else "FAILURE"

    output = f"""
    ============================
    Authorization Test Version 2
   ============================

  Request to "/v2/sentiment"
  | username="{value['username']}"
  | password="{value['password']}"
  | sentence="{value['sentence']}"


   expected result = 200
   Actual code = {status_code}

   ==> {result}
   """

    print(output)



# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)