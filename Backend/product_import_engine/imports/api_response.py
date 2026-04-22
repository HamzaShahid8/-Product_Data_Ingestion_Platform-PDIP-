from rest_framework.response import Response

def api_response(success = True, message = '', data = None, errors = None, meta = None, status_code = 200):
    return Response(
        {
            'success': success,
            'message': message,
            'data': data or {},
            'errors': errors or [],
            'meta': meta or {},
        },
        status=status_code
    )