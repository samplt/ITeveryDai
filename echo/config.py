TG_TOKEN = "5259909775:AAHUD6iqtRxhvUMvmr-esPMTIDhQ50g_yYk"
TG_API_URL = "https://telegg.ru/orig/bot"

LOGGING = {
    'disable_existing_loggers': True,
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s| %(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter' : 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate' : False,
        },
    },
}
logging.config.dictConfig(LOGGING)
