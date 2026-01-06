with base as (
    select
        mal_id, 
        title,
        anime_type,
        anime_status,
        episodes,
        season, 
        release_year

    -- creates a dependency between stg_anime and dim_anime
    from {{ ref('stg_anime') }}
)

select * from base