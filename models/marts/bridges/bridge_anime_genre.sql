
with anime_genres as (
    select
        mal_id,
        genre
    from {{ref ('stg_anime_genres')}}
    ),

    joined as (
        select
            ag.mal_id,
            dg.genre_id
        from anime_genres ag
        join {{ ref('dim_genre') }} dg
            on ag.genre = dg.genre_name
    ),

    base as (
        select distinct
            mal_id,
            genre_id    
        from joined
    )

select * from base