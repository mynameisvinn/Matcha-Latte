import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm

POSTGRES_ADDRESS = 'db.panoply.io'  # INSERT YOUR DB ADDRESS
POSTGRES_PORT = '5439'
POSTGRES_USERNAME = 'vin.tang@gmail.com'
POSTGRES_PASSWORD = 'Cobalt27!'
POSTGRES_DBNAME = 'playerslounge_prod'  # CHANGE THIS TO YOUR DATABASE NAME


def fetch_dataset(title: str) -> pd.DataFrame:
    """Fetch historical outcomes and returns a dataframe.
    """
    query = _format_query(title)
    df = _fetch_panoply(query)
    data = query2outcomes(df)
    return data


def _fetch_panoply(query):
    """Retrieves raw data from Panoply database.
    """
    postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'.
        format(username=POSTGRES_USERNAME,
            password=POSTGRES_PASSWORD,
            ipaddress=POSTGRES_ADDRESS,
            port=POSTGRES_PORT,
            dbname=POSTGRES_DBNAME))

    cnx = create_engine(postgres_str)
    return pd.read_sql_query(query, cnx)


def _format_query(title):
    """Construct query string given game title.
    """
    query = """
    select contests.id, contests.__updatetime, contests.type, contests_plrsbefore.plr, contests.winner, contests.loser, contests_plrsbefore.userid, contests.status
    from contests
    inner join contests_plrsbefore
    on contests.id = contests_plrsbefore.contests_id
    where contests.console_game = '{}'
    """.format(title)
    
    return query


def query2outcomes(df):
    """Convert raw dataframe into processed dataframe
    """

    lookup = {}  # k=contest id, v=win/loss/time

    for _, row in tqdm(df.iterrows()):
        if row['status'] != "completed" or row['type'] != 'H':
            pass
        else:
            if row['id'] not in lookup.keys():
                if row['userid'] == row['winner']:
                    lookup[row['id']] = {"winner": row['plr']}
                else:
                    lookup[row['id']] = {"loser": row['plr']}
            else:
                if row['userid'] == row['winner']:
                    lookup[row['id']]['winner'] = row['plr']
                else:
                    lookup[row['id']]['loser'] = row['plr']
            lookup[row['id']]['time'] = row['__updatetime']

    contest = []
    winner = []
    loser = []
    time = []

    for k, v in lookup.items():
        contest.append(k)
        winner.append(v['winner'])
        loser.append(v['loser'])
        time.append(v['time'])

    outcomes = {'contest': contest, 'winner': winner, 'loser': loser, 'time': time}
    
    data = pd.DataFrame.from_dict(outcomes)
    return data


