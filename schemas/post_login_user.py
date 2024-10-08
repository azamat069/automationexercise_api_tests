login_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "responseCode": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "responseCode",
        "message"
    ]
}