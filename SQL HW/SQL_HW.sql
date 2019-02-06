
-- HW
-- 1a,1b, 2a,2b and 2C

use sakila;
select first_name,last_name from actor a
select CONCAT(a.first_name,' ',a.last_name) as Actor_Name
from actor a
select a.actor_id,a.first_name,a.last_name from actor a
where a.first_name = 'Joe'
select * from actor a
where a.last_name like '%GEN%'
select * from actor a
where a.last_name like '%LI%'
order by 3,2
select c.country_id,c.country from country c
where country in ('Afghanistan','Bangladesh','China')

-- 3a,3b,4a,and 4b
ALTER TABLE actor
ADD description BLOB NOT NULL;
ALTER TABLE actor
DROP COLUMN description
select a.last_name,count(*) as names_count
from actor a
group by 1
HAVING names_count = 2;

-- 4C and 4D
select a.actor_id,a.first_name,a.last_name from actor a
where a.actor_id = 172;
UPDATE actor
SET first_name = 'GROUCHO'
WHERE actor_id = 172;
select a.actor_id,a.first_name,a.last_name from actor a
where a.actor_id = 172;
UPDATE actor
SET first_name = 'GROUCHO'
WHERE actor_id = 172;
select a.actor_id,a.first_name,a.last_name from actor a
where a.actor_id = 172;

-- 5a create table
CREATE TABLE address (
  address_id smallint(5) NOT NULL,
  address VARCHAR(50),
  address2 VARCHAR(50),
  district VARCHAR(20),
  city_id smallint(5),
  postal_code VARCHAR(10),
  phone VARCHAR(20),
  location geometry,
  last_update timestamp
);

-- 6a,6b

select s.first_name,s.last_name,a.address
from staff s join address a on s.address_id =a.address_id
select s.first_name,s.last_name,sum(p.amount) as total_payment
from staff s join payment p on s.staff_id =p.staff_id
group by 1,2

-- 6c
select f.title,count(fa.actor_id) as Actor_count
from film_actor fa inner join film f on fa.film_id =f.film_id
group by 1
-- 6d
select f.title,count(i.film_id) as Number_of_movies
from film f inner join inventory i on f.film_id =i.film_id
group by 1
having f.title='Hunchback Impossible'
-- 6e
select c.first_name,c.last_name,sum(p.amount) as Total_amount
from customer c join payment p on c.customer_id =p.customer_id 
group by 1,2
order by 2 asc

-- 7b and 7c
SELECT title from film
where language_id in
(
	select language_id from language
	where name ='english'
)
and title like 'K%'or title like 'Q%'; 

select first_name,last_name from actor
where actor_id in
(
	select actor_id from film_actor
    where film_id in
    (
		select film_id from film
        where title = 'Alone Trip'
	)
);

-- 7C
select * from country
select c.first_name,c.last_name,c.email from customer c
join address a on c.address_id=a.address_id
join city ci on a.city_id=ci.city_id
join country co on ci.country_id=co.country_id
where co.country = 'Canada'

-- 7d
select * from category
select f.title,c.name from film f
join film_category fc on f.film_id=fc.film_id
join category c on fc.category_id = c.category_id
where name = 'Family'

-- 7e
select f.title, count(r.rental_id) as rental_count from film f
join inventory i on f.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
group by 1
order by 2 DESC

--7f
select * from store
select st.store_id, sum(p.amount) as Total_amount from payment p
join staff s on p.staff_id = s.staff_id
join store st on s.store_id = st.store_id
group by 1

-- 7g
select st.store_id, c.city,co.country from store st
join address a on st.address_id=a.address_id
join city c on a.city_id=c.city_id
join country co on c.country_id=co.country_id

-- 7h
select c.name,sum(p.amount) as total_amount from category c
join film_category fc on c.category_id=fc.category_id
join inventory i on fc.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
join payment p on r.customer_id=p.customer_id
group by 1
order by 2 desc limit 5;

-- 8a,8b and 8c
use sakila;
CREATE VIEW Top_Genre_Revenue AS
select c.name,sum(p.amount) as total_amount from category c
join film_category fc on c.category_id=fc.category_id
join inventory i on fc.film_id=i.film_id
join rental r on i.inventory_id=r.inventory_id
join payment p on r.customer_id=p.customer_id
group by 1
order by 2 desc limit 5;

select * from Top_Genre_Revenue
DROP VIEW Top_Genre_Revenue;