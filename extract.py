"""Extracting PDFs from website"""

import requests

for n in range(2037, 2103):
    url = f"http://www.academieroyale.be/Academie/documents/FichierPDFBiographieNationaleTome{n}.pdf"
    r = requests.get(url)
    if r.status_code == 200:
        with open(f"data/bn/{n}.pdf", "wb") as f:
            f.write(r.content)
    else:
        print(f"{n}: {r.status_code}")

"""for n in range(2103, )
    url = f"http://www.academieroyale.be/Academie/documents/FichierPDFNouvelleBiographieNational{n}.pdf"""
