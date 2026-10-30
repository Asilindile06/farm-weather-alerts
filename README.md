# farm-weather-alerts

A serverless AWS system that sends bilingual (isiZulu and English) weather alerts to farmers before dangerous weather arrives.

## The Problem

Farmers depend on the weather, and extreme events like heavy rain, floods, heatwaves and frost can destroy crops and livestock in a single night. Many farmers, especially in rural areas such as KwaZulu-Natal, don't get warnings in time or in the language they are most comfortable with. A forecast is only useful if it reaches the farmer early and is easy to understand.

## The Solution

The system checks the weather forecast automatically on a schedule. When a forecast crosses a danger limit for a farm area, it sends a clear alert in both isiZulu and English by email.

## How It Works (deployed version)

1. A timer (AWS EventBridge) triggers the system every 6 hours.
2. A Python function (AWS Lambda) fetches the rain forecast for each farm area from Open-Meteo.
3. Each day's forecast is compared with the danger limit (set with an environment variable, 50 mm by default).
4. For every dangerous day, the function builds a bilingual alert (isiZulu first, then English).
5. The alert is published to an AWS SNS topic, which emails everyone subscribed to it.

```
EventBridge timer  ->  Lambda (Python)  ->  SNS topic  ->  Email
                          |
                          +-> Open-Meteo forecast API
```

The region used is Europe (Stockholm), `eu-north-1`.

## Local Version

The logic was first built and tested on a laptop, before moving to AWS:

- `src/fetch_forecast.py`: fetches the daily rain forecast for one location
- `src/danger_check.py`: decides which days are dangerous
- `src/messages.py`: builds the isiZulu and English alert text
- `src/alerts.py`: reads farmers from `data/farmers.json` and prints alerts for each
- `src/config.py`: danger limit and farm locations
- `tests/`: automated tests with pytest

To run it locally:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python src/alerts.py
python -m pytest
```

## Deployed Version

`src/lambda_function.py` is the AWS Lambda version of the same logic. It uses Python's built-in `urllib` instead of `requests`, so it needs no extra packaging. Its settings come from environment variables:

| Variable | Purpose |
|---|---|
| `RAIN_LIMIT_MM` | Danger limit in millimetres (50 normally, lowered for demos) |
| `SNS_TOPIC_ARN` | The SNS topic the alerts are published to |

## Tech Stack

- Python
- AWS Lambda
- AWS EventBridge
- AWS SNS
- pytest
- Git and GitHub

## Design Decisions

- **Serverless:** there is no server to run or pay for while idle, and a job that runs every few hours suits Lambda.
- **Open-Meteo:** the forecast service is free for non-commercial use and needs no API key, so there is no secret to leak.
- **Built locally first:** the logic was easier to test and fix on a laptop before adding AWS.
- **Configuration in one place:** the danger limit and locations are kept in settings and not scattered through the code. On AWS the limit is an environment variable, so it can change without editing code.
- **Missing values are treated as safe:** the weather service sometimes returns no value for a day, so the check returns "not dangerous" instead of crashing.
- **`urllib` instead of `requests` on Lambda:** it is built into Python, so the function needs no bundled libraries.
- **Least-privilege permission:** the Lambda's role can only publish to the one SNS topic it needs.
- **Email alerts instead of SMS:** email is free within SNS limits and quick to set up, while SMS costs money per message.
- **Limit of 50 mm:** this is a starting value, not an official warning level. It should be checked against South African Weather Service rainfall warning levels and adjusted per crop.
- **Account rebuilt after an MFA lockout:** access to the first AWS account was lost when the authenticator app was on a replaced phone, so the project was rebuilt on a new account. The lesson is to register more than one MFA device.
- **Minimum viable cloud version:** because of that lockout, the deployed version was kept small. The farm locations are written into the Lambda code, and alerts go to the email address subscribed to the SNS topic. The local version reads farmers from a file.

## Project Status

Working end to end on AWS: the timer triggers the Lambda, which fetches the forecast, checks it against the limit, and sends bilingual email alerts through SNS. Planned improvements are listed in the roadmap below.

## Roadmap

- [x] Create repository and project setup
- [x] Fetch forecast for one location
- [x] Add danger-limit check
- [x] Add bilingual isiZulu/English alert messages
- [x] Add sample farmers file
- [x] Add tests
- [x] Deploy to AWS Lambda
- [x] Send alerts with SNS email
- [x] Add EventBridge timer
- [ ] Store farmers in DynamoDB, so each farmer gets alerts only for their own area
- [ ] Save an alert history log in S3
- [ ] Add more alert types (heat and frost)
- [ ] Add SMS alerts
- [ ] Final architecture diagram

## How This Was Built

AI tools were used for guidance and code suggestions. The code was typed in, run, tested and committed step by step, and the design decisions above were made and can be explained by the author.

## Credits

Weather data by [Open-Meteo.com](https://open-meteo.com/).

## Author

Silindile
GitHub: [Asilindile06](https://github.com/Asilindile06)
LinkedIn: [silindile-annastacia](https://www.linkedin.com/in/silindile-annastacia)

WTC-HXHCHDGK