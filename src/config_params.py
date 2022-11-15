from types import SimpleNamespace as sn

STATUS_CODES = dict(
    OK = 200,
    CREATED = 201,
    ACCEPTED = 202,
    NO_CONTENT = 417,
    NO_CONTENT_OK = 204,
    RESET_CONTENT = 205,
    PARTIAL_CONTENT = 206,
    BAD_REQUEST = 400,
    UNATHORIZED = 401,
    FORBIDDEN = 403,
    NOT_FOUND = 404,
    NOT_ALLOWED = 405,
    NOT_ACCEPTABLE = 406,
    TIMEOUT = 503,
    CONFLICT = 409,
    STOPPED = 410,
    UNSUPPORTED = 415,
    EXPECTATION_FAILED = 417,
    UNPROCESSABLE_ENTITY = 422,
    OPERATION_ERROR = 500,
    NOT_IMPLEMENTED = 501,
    NO_MONITOR = 502,
    UNAVAILABLE = 503,
    MONITOR_TIMEOUT = 504,
)


def init_cfg(app):

    app.config.update(
            STATUS_CODES=sn(**STATUS_CODES),
            HOST= "0.0.0.0",
            PORT= 5000,
            JSON_AS_ASCII = False, #No Ascii, reposne json, utf-8
            JSON_SORT_KEYS = False, # No sort key json in response
             
        )