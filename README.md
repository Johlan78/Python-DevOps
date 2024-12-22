Bonjour, cette appli python/flask tourne sur Azure en tant que Web App.
Elle permet de calculer le BMI et le BMR, le déploiement ce fait grace a un pipeline CI/CD.

L'adresse web du serveur Azure est : https://pythonwebapp-dqfha7eshxgkangz.francecentral-01.azurewebsites.net/

Pour tester le BMI et le BMR vous devez envoyer des requetes http, vous pouvez essayer les commandes suivantes par exemple :

BMI : curl -X POST -H "Content-Type: application/json" -d '{"weight": 70, "height": 1.75}' https://pythonwebapp-dqfha7eshxgkangz.francecentral-01.azurewebsites.net/bmi
BMR : curl -X POST -H "Content-Type: application/json" -d '{"weight": 70, "height": 175, "age": 25, "gender": "male"}' https://pythonwebapp-dqfha7eshxgkangz.francecentral-01.azurewebsites.net/bmr

Merci à vous, cordialement Johlan SLAMA
