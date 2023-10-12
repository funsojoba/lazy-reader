from flask import jsonify


def api_response(status=200, message=None, data=None, errors=None):

    if not any([message, data, errors]):
        raise ValueError("Message, data or errors required")

    response = jsonify(
        {
            "status": "success" if status in [200, 201] else "failure",
            "message": message,
            "data": data,
            "errors": errors,
        }
    )
    response.status_code = status
    return response
