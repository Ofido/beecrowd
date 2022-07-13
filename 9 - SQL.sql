/* 2602 - Select Básico */
Select Name from customers where state = 'RS'

/* 2603 - Endereço dos Clientes */
select name, street from customers where city = 'Porto Alegre'

/* 2604 - Menores que 10 ou Maiores que 100 */
select id, name from products where 100 < price or price < 10

/* 2605 - Representantes Executivos */
select products.name, providers.name from products, providers where products.id_categories = 6 and providers.id = products.id_providers

/* 2606 - Categorias */
select products.id, products.name from categories, products where categories.name like 'super%' and categories.id = products.id_categories

/* 2607 - Cidades em Ordem Alfabética */
select city from providers order by city asc

/* 2608 - Maior e Menor Preço */
select max(price), min(price) from products LIMIT 1

/* 2609 - Produtos por Categorias */
select categories.name as name, SUM(products.amount) as sum from products, categories where categories.id = id_categories group by categories.id

/* 2610 - Valor Médio dos Produtos */
select round(avg(price),2) from products

/* 2611 - Filmes de Ação */
select movies.id, movies.name from movies, genres where genres.id = id_genres and genres.description like 'Action'

/* 2613 - Filmes em Promoção */
select movies.id, movies.name from movies, prices where prices.id = id_prices and prices.value < 2.00

/* 2614 - Locações de Setembro */
select name, rentals_date from rentals, customers where customers.id = id_customers and rentals_date >= '2016-09-01' and rentals_date <= '2016-09-31'
