-- exploding genres

with base as (
    select
        mal_id,
        trim(initcap(genre)) as genre
    from
    -- explode string
        (select
            mal_id,
            unnest(string_to_array(genres,',')) as genre
        from {{ ref('stg_anime') }} ) as g
) 


select * from base