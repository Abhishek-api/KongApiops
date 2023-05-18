import pyrebase
import yaml
import requests


base_path = os.getcwd()
filename = "pipe1.yml"
with open("pipe1.yml") as f:
  file_data =f.read()




# Initialize Firebase app with configuration
config ={
  "apiKey": "AIzaSyAEGVt9PH7mXuCoYzQQTAyiHFIs9iyQfxw",
  "authDomain": "abhishek-kong.firebaseapp.com",
  "projectId": "abhishek-kong",
  "storageBucket": "abhishek-kong.appspot.com",
  "messagingSenderId": "63263581613",
  "appId": "1:63263581613:web:ff2de0a479a06f5b13ad24",
  "measurementId": "G-F2DGX8NWZ5"
}


firebase = pyrebase.initialize_app(config)

storage = firebase.storage()
storage.child("Specs/" + filename).put(file_data)
