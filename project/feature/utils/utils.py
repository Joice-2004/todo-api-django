import urllib.parse
from rest_framework.request import Request


class Utils:

    @staticmethod
    def success_response(message: str = None, data: list | dict = None):
        response = {"status": True}
        if message:
            response["message"] = message
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def warning_response(warning: str, message: str = None, data: list | dict = None):
        response = {"status": True, "warning": warning}
        if message:
            response["message"] = message
        if data is not None:
            response["data"] = data
        return response

    @staticmethod
    def error_response(message: str, error: str | list[str]):
        return {
            "status": False,
            "message": message,
            "error": error
        }


    @staticmethod
    def extract_params(url: str):
        query = url.split('?')
        if len(query) > 1:
            info = urllib.parse.unquote(query[1].strip())
        else:
            info = 'page_num=1'
        return info.split('&'), query[0]

    @staticmethod
    def get_query_params(request: Request):
        query_params = {}
        try:
            url = request.get_full_path()
        except Exception:
            url = request.path

        query, base_url = Utils.extract_params(url=url)

        for item in query:
            try:
                key, value = item.split('=')
            except ValueError:
                key = item
                value = ''
            query_params[key] = value

        return query_params
