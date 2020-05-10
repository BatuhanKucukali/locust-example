# Locust Load Test Example

## Technologies
* [Locust](https://locust.io/)

## Prerequisites
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python](https://www.python.org/)
* [Node.js](https://nodejs.org/en/download/)

## Run this project
1 . Clone project on your machine.
```
git clone git@github.com:BatuhanKucukali/locust-example.git
```
2 . Go to locust-example folder.
```
cd locust-example
```
3 . Go to example-api folder.
```
cd example-api
```
4 . Start test api.
```
npm start
```
5 . Create test user for authentication.
```
curl --location --request POST 'http://localhost:3030/users' \
--header 'Content-Type: application/json' \
--data-raw '{
	"email" : "jone@doe.test",
	"password" : "123456"
}'
```
6 . Go to locust folder.
```
cd ../locust
```
7 . Install dependencies.
```
pip install -r requirements.txt
```
8 . Start locust.
```
locust -f locustfiles/api_user.py
```
9 . Go to locust ui.
```
http://localhost:8089/
```
