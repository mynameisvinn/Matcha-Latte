import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from tqdm import tqdm

POSTGRES_ADDRESS = 'db.panoply.io' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
POSTGRES_PORT = '5439'
POSTGRES_USERNAME = 'vin.tang@gmail.com' ## CHANGE THIS TO YOURPANOPLY/POSTGRES USERNAME
POSTGRES_PASSWORD = 'Cobalt27!' ## CHANGE THIS TO YOUR PANOPLY/POSTGRES PASSWORD
POSTGRES_DBNAME = 'playerslounge_prod' ## CHANGE THIS TO YOUR DATABASE NAME

def fetch(query):
	postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(username=POSTGRES_USERNAME,
	password=POSTGRES_PASSWORD,
	ipaddress=POSTGRES_ADDRESS,
	port=POSTGRES_PORT,
	dbname=POSTGRES_DBNAME))

	cnx = create_engine(postgres_str)

	return pd.read_sql_query(query, cnx)
	