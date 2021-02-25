from Google import Create_Service

CLIENT_SECRET_FILE ='JD_jYj0jkMIxUikzAY5dEfC6'
API_NAME='drive'
API_VERSION ='v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

natinal_parks = ['carpeta']

for natinal_park in national_park:
    file_metadata={
        
        'name': national_park,
        'mimeType': 'application/vnd.google-apps.folder'
        # 'parents':[]
        } 
service.files().create(body=file_metadata).execute()