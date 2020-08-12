class MyMiddleware:
    def __init__(self):
        print('__init__')

    def process_request(self, request):
        print('process_request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print('process_view')

    def process_response(self, request, response):
        print('process_response')
        return response