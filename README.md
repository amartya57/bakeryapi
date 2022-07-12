
# Bakery API

This is a REST Api for a bakery shop cum delivery service. It is built using the Django REST Framework.
### Functionalities :
* Register user, login and logout.
* Create new products and review individual products. (CRUD)
* Place orders by customers. (CRUD)
### Features :
* Token Authentication
* Permissions
* Throttling
* pagination
* Searching
* Ordering

## Base URL
http://bakerybackendapi.herokuapp.com/

### Authorization Endpoints
METHOD | ROUTE | FUNCTIONALITY | ACCESS - ADMIN | ACCESS - USER | ACCESS - ANON 
--- | --- | --- | --- |--- |--- 
POST | account/register/ | Register new user | - | - | - 
POST | account/login/ | Get auth token for user | POST | POST | None 
POST | account/logout/ | Destroy auth token for user | POST | POST | None 


### Product Endpoints
METHOD | ROUTE | FUNCTIONALITY | ACCESS - ADMIN | ACCESS - USER | ACCESS - ANON 
--- | --- | --- | --- |--- |--- 
GET,POST | products/list/ | Get all products, create new products | GET, POST | GET | GET 
GET, PUT, PATCH, DELETE | products/{product_id}/ | Retrieve, Update, Delete a product | GET, PUT, DELETE | GET | None 
GET | products/{product_id}/reviews/ | Get the reviews for a product | GET | GET | GET
POST | products/{product_id}/reviews-create/ | Post reviews for a product | - | POST | None
GET, PUT, PATCH, DELETE | products/reviews/{review_id}/ | Retrieve, Update, Delete a review | - | GET, PUT, DELETE | None

### Order Endpoints  
METHOD | ROUTE | FUNCTIONALITY | ACCESS - ADMIN | ACCESS - USER | ACCESS - ANON 
--- | --- | --- | --- |--- |--- 
GET | orders/list/ | Get all the orders | GET | GET | None 
POST | orders/{product_id}/create/ | Create an order for a product | - | POST | None 
POST | orders/{order_id}/detail/ | Retrieve, Update, Delete an order | GET, PUT, DELETE | GET, PUT, DELETE | None

## Checks in place :
* One user can create one review for a product
* An user can only edit reviews made by him/her
* Admin can only change the delivered status of an order
* An user can only see orders made by him/her. Admin can see all orders
* An user can edit orders only before the delivery.
* An user can create maximum 3 orders per hour.

## Searching and Ordering
* The *products/list/* endpoint support search functionality for name and description. ( *base/products/list/?search=chocolate* )
* The *products/list/* endpoint support ordering based on price ( *base/products/list/?order=price* )