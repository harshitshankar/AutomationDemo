# AutomationDemo - Python Selenium Project

## Features
- Selenium + Pytest
- Page Object Model
- Allure reporting
- Docker-ready
- Jenkins CI/CD ready

## How to Run

1. Install Python, Chrome, ChromeDriver, Docker, Allure
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run tests:

```
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

4. Docker:

```
docker build -t automation-demo .
docker run --rm automation-demo
```
