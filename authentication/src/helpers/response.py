from flask import jsonify


class InvalidResponse(Exception):
    pass


class Response:
    def __new__(cls, data=None, error=None, status_code=200):
        
        cls.validate(data, error)
        return jsonify(
            data=data,
            error=error
        ), status_code

    
    @classmethod
    def validate(cls, data, errors):
        if not any([data, errors]):
            raise InvalidResponse("Both data and errors cannot be None")
        