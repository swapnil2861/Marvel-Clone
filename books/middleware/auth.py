from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        returnurl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('costomer'):
            return redirect(f'login?return_url={returnurl}')
        response = get_response(request)
        return response

    return middleware