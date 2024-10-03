import logging
from requests import Response
import allure
from allure_commons.types import AttachmentType
import json


def add_attach(response: Response):
    allure.attach(body=response.request.url, name="Request url",
                  attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=str(response.status_code), name="Response status",
                  attachment_type=AttachmentType.TEXT, extension="txt")
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response body",
                  attachment_type=AttachmentType.JSON, extension="json")


def add_logs(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


