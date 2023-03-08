import asyncio
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def simple_middleware(get_response):

    if asyncio.iscoroutinefunction(get_response):
        async def middleware(request):
            response = await get_response(request)
            #print(request.META)
            return response
    else:
        def middleware(request):
            response = get_response(request)
            if 'provenance' in request.headers:
                provenance_id = request.headers['provenance']
                print(f'provenance: {provenance_id}')
            # print(request.META)
            return response

    return middleware
