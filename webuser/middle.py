from django.core.cache import cache

class CommonMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        online_ips = cache.get('online_ips',[])
        if online_ips:
            online_ips = cache.get_many(online_ips).keys()

        cache.set(ip,0,5*60)
        if ip not in online_ips:
            online_ips.append(ip)
        cache.set('online_ips',online_ips)
        response = self.get_response(request)
        return response
