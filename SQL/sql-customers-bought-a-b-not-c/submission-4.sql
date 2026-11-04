-- Write your query below
select c.*
from customers c
where c.customer_id in (
    select customer_id
    from orders
    where product_name = 'A'
)
and c.customer_id in (
    select customer_id
    from orders
    where product_name = 'B'
)
and c.customer_id not in (
    select customer_id
    from orders
    where product_name = 'C'
)
order by customer_name