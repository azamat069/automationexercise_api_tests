## Демо проект автоматизации тестирования сайта [automationexercise](https://automationexercise.com/)

---
### Проект представляет собой набор API-тестов покрывающих следующий функционал:
1. Регистрация
2. Авторизация
3. Списки товаров
4. Работа фильтра товаров

---
## Используемый стек:
<p align="left">
<img src="media/python-original-wordmark.svg" width="50" height="50"/>
<img src="media/pytest-original-wordmark.svg" width="50" height="50"/>
<img src="media/Selenium.png" width="50" height="50"/>
<img src="media/jenkins-original.svg" width="50" height="50"/>
<img src="media/AllureReport.png" width="50" height="50"/>

</p>

Проект написан на языке программирования Python, с использованием фреймворков Pytest, Selene.

Реализована удаленная сборка тестов в Jenkins

После прохождения тестов система отправляет краткий отчет в [Telegram](https://t.me/demo_project_notifications)

Так же в Jenkins будет доступен подробный отчет Allure

---
## Инструкция по удаленному запуску тестов:
1. Перейти по ссылке в [сборку](https://jenkins.autotests.cloud/job/qa_guru_14_automationexercise_API_tests/)
2. Нажать Build Now
<img src="media/jenkins_build_now.png"/>

---
## Allure отчет о прохождении тестов
### Общий результат прохождения тестов
<img src="media/allure_general_report.png"/>

### Графики
<img src="media/allure_grafics.png"/>

### Подробный отчет о прохождении
<img src="media/allure_detailed_report.png"/>

---
## Telegram отчет
<img src="media/telegram_allure_report.png"/>

