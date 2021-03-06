import random


# Si sentry est défini, on importe le sdk et configure l'app

import os
sentry_dsn = os.getenv('SENTRY_DSN',None)
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration
    sentry_sdk.init(
        sentry_dsn,
        integrations=[FlaskIntegration()]
        )


from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    #return jsonify({'roll':0})
    return jsonify({'roll':random.randint(1,12)})


print(app)
#print(dir(app))
#print(app.config)

#
# {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None,  'SESSION_REFRESH_EACH_REQUEST': #True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(seconds=43200), 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}
#

@app.route('/error')
def error():
    # 1/0 should not work
    #return jsonify({'roll':1 / 0})
    # en fait, plus une erreur
    return jsonify({'roll':1})
