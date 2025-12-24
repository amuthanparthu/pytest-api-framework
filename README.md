# pytest-api-project

A Python-based API testing framework using Pytest,  Docker and Allure/HTML reports.  Supports CI/CD integration and automated reporting.

# Project Structure


pytest-api-framework/
├── configs/
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh
├── fixtures/
├── reports/
│   ├── allure/
│   └── html/
├── test_data/
├── tests/
├── utils/
├── .gitlab-ci.yml
├── conftest.py
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
└── README.md

# Environment Setup

## Local Python Environment**
1. Clone the repository:

   git clone https://github.com/amuthanparthu/pytest-api-framework.git
   cd pytest-api-framework

2. Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate          # Windows

3. Install dependencies:

   pip install -r requirements.txt

# Running Tests

## Using Docker 
1. Ensure Docker and Docker Compose are installed.

  sudo docker-compose build --no-cache

2. Start services and run tests:

  sudo docker-compose up --abort-on-container-exit --exit-code-from pytest-runner

  * This will spin up required containers (e.g., RabbitMQ, httpbin) and execute your tests.
  * Containers will stop automatically when tests complete.

## With Pytest locally

# Generating and Viewing Reports

1. HTML Reports:

   pytest --html=reports/html/report.html --self-contained-html

   * Open reports/html/report.html in your browser.

2. Allure Reports:

   pytest --alluredir=reports/allure

   allure serve reports/allure

   # If allure is not installed, follow the below steps to install allure in your local setup

   1. sudo wget https://github.com/allure-framework/allure2/releases/download/2.36.0/allure-2.36.0.tgz -O allure.tgz

   2. tar -xvzf allure.tgz

   3. sudo mv allure-2.* /opt/allure

   4. echo 'export PATH=$PATH:/opt/allure/bin' >> ~/.bashrc
      source ~/.bashrc

   5. allure --version

   6. pytest --alluredir=reports/allure

   7. allure serve reports/allure

# CI/CD Integration (GitLab)

1. Place .gitlab-ci.yml in the root of the repository.

2. GitLab will automatically save HTML/Allure reports as artifacts.

# Contact / Contribution

For questions or contributions:

Author: Amutharasan Parthasarathy

Email: amuthanparthu@gmail.com

GitHub: https://github.com/amuthanparthu/pytest-api-framework
