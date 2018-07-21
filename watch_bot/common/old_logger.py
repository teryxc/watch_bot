import logging, os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
 
# create console handler and set level
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# create file handler and set level
handler = logging.FileHandler('debug.log','w',encoding='utf-8',delay='true')
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)