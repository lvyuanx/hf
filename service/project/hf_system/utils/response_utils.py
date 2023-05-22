from rest_framework.response import Response


def response(code: int, msg: int, data):
    res = {
        "code": code,
        "msg": msg,
        "data": data,
    }
    return Response(status=200, data=res)


def response_ok(msg="success", data=None):
    return response(200, msg, data)


def page_ok(paginator, lst, msg="success"):
    page_info = {
        "total": paginator.page.paginator.count,
        "pageSize": paginator.page_size,
        "pageCount": paginator.page.paginator.num_pages,
        "currentPage": paginator.page.number,
        "results": lst,
    }

    return response(200, msg, page_info)


def response_error(msg="error", data=None):
    return response(500, msg, data)


class LResponse:

    def __init__(self,
                 data=None,
                 code=None,
                 msg=''):
        self.code = code
        self.msg = msg
        self.data = data
        self.response = Response

    def result(self, code=None, msg='', data=None):
        data = {
            "code": code,
            "msg": msg,
            "data": data,
        }
        return self.response(status=200, data=data)

    def ok(self, msg='success'):
        return self.result(200, msg, self.data)

    def page_ok(self, paginator, msg="success"):
        page_info = {
            "total": paginator.page.paginator.count,
            "pageSize": paginator.page_size,
            "pageCount": paginator.page.paginator.num_pages,
            "currentPage": paginator.page.number,
            "results": self.data,
        }

        return self.result(200, msg, page_info)

    def error(self, msg='error'):
        return self.result(500, msg, self.data)
