#!/bin/sh
set -e

echo "Waiting for httpbin..."
until curl -sf http://httpbin:80/get > /dev/null; do
  sleep 2
done

echo "Waiting for RabbitMQ..."
until curl -sf http://rabbitmq:15672 > /dev/null; do
  sleep 2
done

echo "All services are up. Running tests..."

pytest \
  --html=reports/report.html \
  --self-contained-html \
  --alluredir=allure-results
