from fastapi import HTTPException, status


class TimeOutExc(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_408_REQUEST_TIMEOUT
        self.detail = "Request Timeout: Please try again!"


class ConnectionExc(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_502_BAD_GATEWAY
        self.detail = "Connection Error: Please check your network and try again!"
