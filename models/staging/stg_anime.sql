-- stg_anime.sql

with base as (
    select 
        mal_id,
        title, 
        s.type AS anime_type,
        episodes, 
        s.status AS anime_status,
        score, 
        scored_by,
        rank, 
        popularity, 
        favorites, 
        season, 
        s.year AS release_year,
        genres
    from {{ source('jikan', 'anime_tbl') }} as s 
)

select * from base