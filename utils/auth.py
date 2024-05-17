from config import conf

def valid_authorization(request):
    authorization_header = request.headers.get('Authorization')
    authorization = conf().get("authorization")
    return authorization_header == authorization
