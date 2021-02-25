import json
import requests
headers = {"Authorization": "Bearer ya29.A0AfH6SMDU7pzOBcEEQ5HdL1aRYoaXRZCe34XrwCTAs88Ov0UcNkepsB2Q9IrikCbesZ0Ze9wCl6TiytXO-2jkHtElDRUzqsi4lFbwbMWQ8CgWh_g_GsggXOWWnCsG3luqVx4a31FpuxolIed2wSLltfX_nnSx"}
para = {
    "name": "dir_prueba.folder",
    "parents":["1s4POsPuo4cv1QIhSR3gUS4sOpvA6A4Jq"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./dir_prueba.folder", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)

