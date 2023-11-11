import cgi

print("Content-Type: text/html; charset=utf-8\n")

html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>page html en python</title>
</head>
<body>
   <h1>Inscription</h1>
    <form method="post" action="result.py"> 
     <p>Prénom :<input type="text" name="prenom"></p> 
     <p>Nom :<input type="text" name="nom"></p> 
     <input type="submit" value="envoyer"></p> 
     </form> 
</body>
</html>
"""

print(html)