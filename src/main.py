import pandas as pd
from jikan import JikanClient
from db import get_db_connection

def run_pipeline():
    # instantiate client
    client = JikanClient()
    
    data = []
    for page in range(1,5):
        anime  = client.get_anime(page)
        data.extend(anime)
    
    engine = get_db_connection()
    anime_df = pd.DataFrame(data)
    anime_df.to_sql(name="anime_tbl", con=engine, if_exists='append')
    
    
    with engine.connect() as conn:
        print("Success!")

if __name__ == "__main__":
    run_pipeline()