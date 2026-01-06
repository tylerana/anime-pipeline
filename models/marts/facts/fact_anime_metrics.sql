with base as (
    select 
    mal_id,
    favorites,
    popularity, 
    rank, 
    score,
    scored_by

    -- creates a dependency between stg_anime and fact_anime_metrics
    from {{ ref('stg_anime') }}
)

-- GOAL: I want to rank rows within each mal_id by favorites, then keeping only the top-ranked row.
-- outer query declares the winner and tells us to "only keep the row that won"
select *
from( 
    -- inner query: compare rows without collapsing them
    select *, 
        row_number() over (partition by mal_id order by favorites desc) as row_num
        from base
    ) as top_mal_id
where row_num = 1
