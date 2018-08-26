import os
import yaml
import logging.config
import logging
import coloredlogs
import pandas as pd

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTROL_PANEL_URL = 'https://www.furaffinity.net/msg/others/'

pd.set_option('display.expand_frame_repr', False)

def dump_df(logger, df, df_name, show_all=False):
    
    logger('{} - {} rows - {} \n {}'.format(df_name, df.shape[0], list(df), df if show_all else df.head(5)))

def get_logger(name):
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    return logger

def setup_logging(default_path=os.path.join(ROOT_DIR, 'common', 'logging.yaml'), default_level=logging.DEBUG, env_key='LOG_CFG'):
    """
    | **@author:** Prathyush SP
    | Logging Setup
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
                coloredlogs.install(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')

setup_logging()