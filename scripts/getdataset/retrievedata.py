'''
purpose: 
'''
import requests

def download_dataset():
  print("DOWNLOADING")

if __name__ == "__main__":
  response = requests.get("http://api.open-notify.org/astros.json")
  print(response)
  # download_dataset()