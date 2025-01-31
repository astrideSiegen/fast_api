import os
import requests

# définition de l'adresse de l'API 
#définition de fast_api'adresse de l'API, avec le service du docker-compose.yml 
api_address = 'fast_api' 
# port de l'API
api_port = 8000


values = [
    {"sentence": "life is beautiful" },
    {"sentence": "that sucks"}

   ]


for value in values:
    for version in ["v1", "v2"]:
        r = requests.get(
                    url = f"http://{api_address}:{api_port}/{version}/sentiment",
            params={
                "username": "alice",
                "password": "wonderland",
                "sentence": value["sentence"],
            }
        )
        print(f"Testing user Alice with password wonderland on version {version}")
        print("response:", r.json())
    
         # # statut de la requête
        status_code = r.status_code
        result = "SUCCESS" if status_code == 200 else "FAILURE"

        # Extract JSON data from the response to get the score
        data = r.json()

        output = f"""
        ============================
        Content Test
        ============================

        Request to "/{version}/sentiment"
        | username= "alice"
        | password= "wonderland"
        | sentence = {value['sentence']}
        | score = {data['score']}

        expected result = 200
        Actual code = {status_code}

        ==> {result}
        """

        print(output)

#impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)