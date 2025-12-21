import requests
import time
from typing import Dict, Any, Optional, List

class JikanClient:
    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4"
        # session is used to keep the connection open
        self.session = requests.Session()
        
    def get_anime(self, page: int = 1) -> List[Dict[str, Any]]:
        """
        Fetches metadata for single anime ID.
        Retries on rate limits (429).
        """
        
        endpoint = f"{self.base_url}/top/anime"
        params = {"page": page, "limit": 25}
        
        # request
        response = self.session.get(endpoint, params=params)
        
        # rate limits 
        if response.status_code == 429:
            print(f"Rate limit reached on page {page}. Retrying in 2 seconds ...")
            time.sleep(2)
            response = self.session.get(endpoint, params=params)
          
        # in case of 404 or 500  
        response.raise_for_status()
        data = response.json().get("data", [])
        
        cleaned_data = [self._parse_anime(item) for item in data]
        return cleaned_data
    
    def _parse_anime(self, item:Dict[str, Any]) -> Dict[str, Any]:
        # Starting a function with "_" signals it's private.
        # Takes the API data and returns the fields needed.
        genres_raw = item.get("genres", [])
        genres = ", ".join([g["name"] for g in genres_raw]) if genres_raw else "Unknown"
        
        return {
            "mal_id": item.get("mal_id"),
            "title": item.get("title"),
            "type": item.get("type"),
            "episodes": item.get("episodes"),
            "status": item.get("status"),
            "score": item.get("score"),
            "scored_by": item.get("scored_by"),
            "rank": item.get("rank"),
            "popularity": item.get("popularity"),
            "favorites": item.get("favorites"),
            "season": item.get("season"),
            "year": item.get("year"),
            "genres": genres
        }
        
if __name__ == "__main__":
    client = JikanClient()
    print("Fetching Page 1 ...")
    anime_list = client.get_anime(1)
    print(f"Successfully fetched {len(anime_list)} anime.")
    print(anime_list[0])