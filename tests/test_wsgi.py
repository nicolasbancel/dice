from flask_testing import TestCase
from wsgi import app
# on import la variable app (l'application)

# faut que fonction commence par test_ pour que nose comprenne

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_one_roll(self):
        roll = self.client.get('/').json['roll']
        ## get : fait la requête HTTP. Puis valeur de la clé roll.
        self.assertIsInstance(roll, int) # c'est un entier
        self.assertGreater(roll,0) # Plus grand que 0
        self.assertLess(roll,7) # Moins grand que 7
