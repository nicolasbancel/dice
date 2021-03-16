
# Run the tests
pipenv run nosetests

# Diff between files
git diff Pipfile



##### SENTRY // ERROR MANAGEMENT #####

## On a créé une erreur sur la route "/error"
# http://localhost:5000/error

##### SENTRY #####
# existe bien dans les ressources

https://dashboard.heroku.com/apps/calm-cove-18496/resources
https://sentry.io/organizations/calm-cove-18496/issues/?project=5679689

##### ERREUR EN PROD #####
https://calm-cove-18496.herokuapp.com/error

# Pull request

# Possible de commenter par ligne de code
# GitHub issues : Issues to reproduce the bug
# Fixes bug No 2 : bug number (-41:48)


###### PUSH VERS HEROKU ######
git push heroku main # deploiement manuel


# Commandes de base heroku

# voir l'app:
heroku open

heroku logs --tail

# Commandes de base heroku

# App can be found here
# https://calm-cove-18496.herokuapp.com/

# Run the web server
# Just execute in shell this script belows
FLASK_ENV=development pipenv run flask run
# Head to http://localhost:5000/

####### USE ADDONS #######
heroku addons:create sentry:f1
