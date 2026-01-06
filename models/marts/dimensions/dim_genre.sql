-- dim genre has exactly one row per unique genre.

with distinct_genres as (
    select
        distinct genre as genre_name
    
    from {{ ref('stg_anime_genres') }}
),

numbered_genres as (
    select
        row_number() over (order by genre_name) as genre_id,
        genre_name
    
    from distinct_genres
)

select *
from numbered_genres