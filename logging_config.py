import logging
import logging.config


def setup_logging():
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG',  # Логирование от уровня DEBUG и выше
            },
            # 'file': {
            #     'class': 'logging.FileHandler',
            #     'formatter': 'default',
            #     'filename': 'app.log',
            #     'level': 'ERROR',  # Логирование от уровня ERROR и выше
            # },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',  # Уровень для корневого логгера
        },
        'loggers': {
            'app': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            # 'module1': {
            #     'handlers': ['console', 'file'],
            #     'level': 'DEBUG',  # Логгер module1 будет записывать DEBUG и выше в консоль и ERROR и выше в файл
            #     'propagate': False,
            # },
            # 'module2': {
            #     'handlers': ['console'],
            #     'level': 'ERROR',  # Логгер module2 будет записывать только ERROR и выше в консоль
            #     'propagate': False,
            # },
        },
    })
