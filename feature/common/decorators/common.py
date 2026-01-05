from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from feature.common.utils import Utils
from django.db.models.query import QuerySet


class Common:
    def __init__(self, response_handler=None):
        self.response_handler = response_handler



    def exception_handler(self, func):
        def wrapper(*args, **kwargs):
            try:
                response = func(*args, **kwargs)

                if (
                    self.response_handler
                    and isinstance(response, Response)
                    and isinstance(response.data, dict)
                    and "data" in response.data
                ):
                    raw_data = response.data["data"]

                    if hasattr(raw_data, "_meta"):
                        serializer = self.response_handler(raw_data)
                        response.data["data"] = serializer.data

                    elif isinstance(raw_data, (list, QuerySet)) and raw_data and hasattr(raw_data[0], "_meta"):
                        serializer = self.response_handler(raw_data, many=True)
                        response.data["data"] = serializer.data

                return response

            except ValidationError as ve:
                return Response(
                    Utils.error_response("Validation error", ve.detail),
                    status=status.HTTP_400_BAD_REQUEST
                )

            except Exception as e:
                return Response(
                    Utils.error_response("Something went wrong", str(e)),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return wrapper
