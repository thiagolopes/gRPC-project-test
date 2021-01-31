# A gRPC project

## About
This project implement two microservices that together powers an web page that displays a product list with custom discounts per user.

### The Python project
This project is responsible for serve a RESTful API with a product resource, this resource will show the discounts available per user based on gRPC call to a "discount API" and apply any rules to them

#### Setup
To run this project you will need installed:
- python 3.8.5 or higher
- poetry
- and any SGDB to use in API

Follow steps:
- `make install-deps` to install all dependencies
- `cp local.env .env`, and update the variables with your settings
- `make migrate` to apply the migrations in database
- Create a user:
  - You can use `make create-user` or use `/admin` to access the admin page with superuser
- To generate a api token you need generate in `/api-auth` with a payload: `{"username": X, "password": Y}`
  - After that you will recive the token and can be able to use in `Authorization` header with value `Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

Finally, to run: `make run`

#### Docs:
The project has one resource: `/v1/products` to access all products, the payload will show the discounts avalible if the request has a `Authorization`


### The Go project
This project is a gRPC server, then applies a series of discounts to an order.

#### Setup
To run this project you will need installed:
- go 1.15.7 (tested in Linux)

Follow steps:
- `make tools` to install tools to be used in development
- `make build` to build the project
- `cp local.env .env`, and update the variables with your settings

Finally, to run binary: `./bin/promotion`
