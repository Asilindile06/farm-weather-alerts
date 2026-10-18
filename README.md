# farm-weather-alerts

A serverless AWS system that sends bilingual (isiZulu and English) weather alerts to farmers
before dangerous weather arrives.

## The Problem

Farmers depend on the weather, and extreme events like heavy rain, floods, heatwaves and 
frost can destroy crops and livestock in a single night. Many farmers, especially in rural 
areas such as KwaZulu-Natal, don't get warnings in time or in a language they are most
comfortable with. A forecast is only useful if it reaches the farmer early and is easy
to understand.

## The Solution

This system checks the weather forecast automatically on a schedule. When a forecast crosses 
a danger limit for a farmer's area, it sends a clear alert in both isiZulu and English.
Every alert is also saved so there is a record of what was sent and when.

## How It Works

1. A timer (AWS EventBridge) triggers the system every few hours.
2. A Python function (AWS Lambda) loads the list of farmers and their areas from a 
database (AWS DynamoDB).
3. For each area, the function fetches the latest weather forecast.
4. The forecast is compared against danger limits, for example heavy rainfall.
5. If a limit is crossed, an alert is sent (AWS SNS) in isiZulu and English.
6. The alert is saved to storage (AWS S3) as a history log.

## Tech Stack

- Python
- AWS Lambda
- AWS EventBridge
- AWS DynamoDB
- AWS SNS
- AWS S3
- Git and GitHub

## Project Status

Work in progress. Currently setting up the project and building the weather-fetching logic
locally before moving it to AWS.

## Roadmap

- [x] Create repository and project setup
- [ ] Fetch forecast for one location
- [ ] Add danger-limit check
- [ ] Add bilingual isiZulu/English alert messages
- [ ] Add sample farmers file
- [ ] Add tests
- [ ] Deploy to AWS Lambda
- [ ] Connect DynamoDB, SNS and S3
- [ ] Add EventBridge timer
- [ ] Final documentation and architecture diagram

## Author

Silindile
GitHub: [Asilindile06](https://github.com/Asilindile06)
LinkedIn: [silindile-annastacia](https://www.linkedin.com/in/silindile-annastacia)



WTC-HXHCHDGK