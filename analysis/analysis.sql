/*
 * a) calculate top 25 most common 'makes'
   b) calculate most common 'Color' for each 'Make' 
   c) find the first ticket issued for each 'Make'
 */
-- a) calculate top 25 most common 'makes'
-- 5.883 seconds
select 
  Make
  , count(*) _count
from vehicles
group by Make
order by _count DESC
limit 25;

-- b) calculate most common 'Color' for each 'Make' 
-- 4.332s
-- fun note - using QUALIFY with Snowflake would make this even faster :)
select
  Make
  , Color
from (
  select 
    Make
    , Color
    , ROW_NUMBER() OVER (PARTITION BY Make ORDER BY _count DESC) as color_rank
  from ( 
    select 
      Make
      , Color
      , count(*) _count
    from vehicles
    group by Make, Color
  )
  where Color IS NOT NULL
)
where color_rank = 1;

-- c) find the first ticket issued for each 'Make'
-- 9.718s
select
  Make
  , "Ticket number"
  , "Issue Date"
from (
  select 
    Make
    , "Ticket number"
    , "Issue Date"
    , ROW_NUMBER() OVER (PARTITION BY Make ORDER BY "Issue Date") as ticket_rank
  from vehicles
)
where ticket_rank = 1
order by Make;