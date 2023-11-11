import cgitb
import cgi
cgitb.enable()
form = cgi.FieldStorage()
if form.getvalue("prenom")!=None:
    prenom = form.getvalue("prenom")
    nom = form.getvalue("nom")
else:
    raise Exception("pseado non transmit")
print("Content-Type: text/html")
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>page html en python</title>
</head>
<body>
    <p>Bien enregistre</p>
</body>
</html>
"""

print(html)
print(f"votre nom et prenom : {prenom} {nom}")