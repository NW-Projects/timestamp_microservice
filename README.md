# timestamp_microservice

This is an adaptation of FCC backend end development and API exercises, written in Python and FastAPI. 

The instructions included creating an API that could do the following:
1. A request to /api/{date} with a valid date should return a JSON object with a unix key that is a Unix timestamp of the input date in milliseconds
2. A request to /api/{date} with a valid date should return a JSON object with a utc key that is a string of the input date in the format: Thu, 01 Jan 1970 00:00:00 GMT
3. A request to /api/1451001600000 should return { unix: 1451001600000, utc: "Fri, 25 Dec 2015 00:00:00 GMT" }
4. The project can handle dates that can be successfully parsed by strptime()
5. If the input date string is invalid, the api returns an object having the structure { error : "Invalid Date" }
6. An empty date parameter should return the current time in a JSON object with a unix key
7. An empty date parameter should return the current time in a JSON object with a utc key