from rest_framework.response import Response


class StandardResponse(Response):
    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super(StandardResponse, self).__init__(data, status, template_name, headers, exception, content_type)
