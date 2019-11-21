{"filter":false,"title":"settings.py","tooltip":"/THIRT13N/settings.py","undoManager":{"mark":38,"position":38,"stack":[[{"start":{"row":53,"column":61},"end":{"row":54,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":54,"column":0},"end":{"row":54,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":54,"column":4},"end":{"row":54,"column":48},"action":"insert","lines":["'whitenoise.middleware.WhiteNoiseMiddleware'"],"id":3}],[{"start":{"row":54,"column":48},"end":{"row":54,"column":49},"action":"insert","lines":[","],"id":4}],[{"start":{"row":135,"column":0},"end":{"row":137,"column":1},"action":"remove","lines":["STATICFILES_DIRS = [","    os.path.join(BASE_DIR, \"static\")","]"],"id":5},{"start":{"row":135,"column":0},"end":{"row":138,"column":0},"action":"insert","lines":["STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')",""]}],[{"start":{"row":134,"column":0},"end":{"row":138,"column":0},"action":"remove","lines":["# enable static files","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')",""],"id":6}],[{"start":{"row":124,"column":0},"end":{"row":125,"column":23},"action":"remove","lines":["","STATIC_URL = '/static/'"],"id":7},{"start":{"row":124,"column":0},"end":{"row":128,"column":0},"action":"insert","lines":["# enable static files","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')",""]}],[{"start":{"row":124,"column":0},"end":{"row":125,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":137,"column":0},"end":{"row":138,"column":0},"action":"remove","lines":["",""],"id":9},{"start":{"row":136,"column":1},"end":{"row":137,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":14,"column":74},"action":"insert","lines":["# import at the top","import dj_database_url","# then...","DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}"],"id":11}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":12}],[{"start":{"row":15,"column":74},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":13}],[{"start":{"row":14,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["# then...","DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}",""],"id":14},{"start":{"row":13,"column":22},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":19},"action":"remove","lines":["","# import at the top"],"id":15}],[{"start":{"row":86,"column":5},"end":{"row":87,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":87,"column":0},"end":{"row":87,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":87,"column":4},"end":{"row":87,"column":66},"action":"insert","lines":["{'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}"],"id":17}],[{"start":{"row":87,"column":5},"end":{"row":88,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":88,"column":0},"end":{"row":88,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":88,"column":4},"end":{"row":88,"column":8},"action":"remove","lines":["    "],"id":19}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"remove","lines":["    "],"id":20},{"start":{"row":87,"column":5},"end":{"row":88,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":87,"column":38},"end":{"row":87,"column":64},"action":"remove","lines":["<DATABASE_URL_FROM_HEROKU>"],"id":21},{"start":{"row":87,"column":38},"end":{"row":87,"column":190},"action":"insert","lines":["postgres://rlbwgnnahhgzgz:eac4b64641ada379dd7e3ea96b33c0ae6c2f1061064de874647b0172b915810a@ec2-54-235-167-210.compute-1.amazonaws.com:5432/dc05u9ph4gpes"]}],[{"start":{"row":87,"column":190},"end":{"row":87,"column":191},"action":"insert","lines":["'"],"id":22}],[{"start":{"row":87,"column":16},"end":{"row":87,"column":17},"action":"insert","lines":["'"],"id":23}],[{"start":{"row":87,"column":16},"end":{"row":87,"column":17},"action":"remove","lines":["'"],"id":24}],[{"start":{"row":87,"column":38},"end":{"row":87,"column":39},"action":"insert","lines":["'"],"id":25}],[{"start":{"row":86,"column":5},"end":{"row":86,"column":6},"action":"insert","lines":[","],"id":26}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":1},"action":"remove","lines":["}"],"id":27}],[{"start":{"row":82,"column":12},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":28}],[{"start":{"row":83,"column":0},"end":{"row":83,"column":4},"action":"insert","lines":["    "],"id":29}],[{"start":{"row":84,"column":0},"end":{"row":84,"column":4},"action":"remove","lines":["    "],"id":30},{"start":{"row":83,"column":5},"end":{"row":84,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":87,"column":193},"end":{"row":89,"column":4},"action":"insert","lines":["","        ","    "],"id":31}],[{"start":{"row":89,"column":5},"end":{"row":90,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"remove","lines":["    "],"id":33}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"insert","lines":["]"],"id":34}],[{"start":{"row":82,"column":12},"end":{"row":82,"column":14},"action":"insert","lines":["[]"],"id":35}],[{"start":{"row":82,"column":13},"end":{"row":82,"column":14},"action":"remove","lines":["]"],"id":36}],[{"start":{"row":89,"column":5},"end":{"row":89,"column":6},"action":"insert","lines":[","],"id":37}],[{"start":{"row":82,"column":0},"end":{"row":90,"column":1},"action":"remove","lines":["DATABASES = [","    {'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    },","    {'default': dj_database_url.parse('postgres://rlbwgnnahhgzgz:eac4b64641ada379dd7e3ea96b33c0ae6c2f1061064de874647b0172b915810a@ec2-54-235-167-210.compute-1.amazonaws.com:5432/dc05u9ph4gpes')","        ","    },","]"],"id":38},{"start":{"row":82,"column":0},"end":{"row":82,"column":74},"action":"insert","lines":["DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}"]}],[{"start":{"row":82,"column":46},"end":{"row":82,"column":72},"action":"remove","lines":["<DATABASE_URL_FROM_HEROKU>"],"id":39},{"start":{"row":82,"column":46},"end":{"row":82,"column":47},"action":"insert","lines":["\""]},{"start":{"row":82,"column":47},"end":{"row":82,"column":48},"action":"insert","lines":["\""]}],[{"start":{"row":82,"column":47},"end":{"row":82,"column":199},"action":"insert","lines":["postgres://rlbwgnnahhgzgz:eac4b64641ada379dd7e3ea96b33c0ae6c2f1061064de874647b0172b915810a@ec2-54-235-167-210.compute-1.amazonaws.com:5432/dc05u9ph4gpes"],"id":40}]]},"ace":{"folds":[],"scrolltop":1657.5,"scrollleft":0,"selection":{"start":{"row":82,"column":199},"end":{"row":82,"column":199},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":77,"state":"start","mode":"ace/mode/python"}},"timestamp":1574324067989,"hash":"770537e20aa3ffde261200f8a8f23514e8a768e8"}