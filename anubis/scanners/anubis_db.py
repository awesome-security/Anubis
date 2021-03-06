from json import dumps, loads

import requests

from anubis.utils.ColorPrint import ColorPrint


def search_anubisdb(self, target):
  print("Searching Anubis-DB")
  res = requests.get("https://jonlu.ca/anubis/subdomains/" + target)

  if res.status_code == 200 and res.text:
    subdomains = loads(res.text)
    for subdomain in subdomains:
      if subdomain not in self.domains:
        self.domains.append(subdomain)


def send_to_anubisdb(self, target):
  print("Sending to AnubisDB")
  data = {'subdomains': dumps(self.domains)}
  res = requests.post("https://jonlu.ca/anubis/subdomains/" + target, data=data)
  if res.status_code != 200:
    ColorPrint.red("Error sending results to AnubisDB - Status Code: " + str(
      res.status_code))
