# Anime Pipeline v2

A Dockerized ELT pipeline that ingests MyAnimeList data via the Jikan API, loads it into Postgres, and models analytics-ready tables using dbt.


## Architecture Overview

- Python ingests data directly from the Jikan (MyAnimeList) API into Postgres
- Postgres runs in a Docker container
- dbt Core (dbt-postgres) runs in a separate container
- dbt models transform raw data into analytics-ready dimensions and facts

All components are orchestrated locally using Docker Compose.



## Tech Stack

- Python (API ingestion)
- Postgres
- dbt Core (dbt-postgres 1.7.9)
- Docker & Docker Compose


## Data Modeling
The warehouse follows a star-schema-inspired design:

### Staging Models (Views)
- `stg_anime` (view)
- `stg_anime_genres` (view)

### Dimension Tables
- `dim_anime`
  One row per `mal_id`
- `dim_genre`
  One row per genre, with surrogate `genre_id`
  
### Fact Table
- `fact_anime_metrics`
  One row per `mal_id`, with deterministic deduplication

### Bridge Table
- `bridge_anime_genre`
  Many-to-many relationship between anime and genres

## Data Quality & Testing
Data quality is enforced using dbt tests, all of which are currently passing.

Tests include:

- `unique` and `not_null` contraints on primary keys
- Referential integrity checks:
  - `bridge_anime_genre.mal_id -> dim_anime.mal_id`
  - `bridge_anime_genre.genre_id -> dim_genre.genre_id`
- Composite uniqueness enforced on `(mal_id, genre_id)` in the bridge table

These tests ensure consistent grain, valid relationships, and reliable downstream

## Running the Project

### Prerequisites
- Docker 
- Docker Compose

### Run the pipeline

```bash
docker compose up -d db
docker compose run --rm dbt dbt build
