"""
Get request information utilities.
"""
import logging

from fastapi import Request
from reflex.state import MutableProxy

from .time_utils import utcnow


def get_request_info(request) -> dict:
    """
    Reads the headers of a request.
    params:
        ! request: Request
            The request made to get the headers.
    """
    def get_from_request() -> dict:
        logging.debug('Getting headers from request.')
        return dict(
            browser=request.headers.get('user-agent'),
            ip=request.client.host,
            path=request.url.path,
            method=request.method.lower(),
            client=request.headers.get('x-client') if 'x-client' in request.headers else f'api-1.0',
            latitude=request.headers.get('x-latitude') if 'x-latitude' in request.headers else 0.0,
            longitude=request.headers.get('x-longitude') if 'x-longitude' in request.headers else 0.0,
            altitude=request.headers.get('x-altitude') if 'x-altitude' in request.headers else 0.0,
            language=request.headers.get('x-language') if 'x-language' in request.headers else 'english',
            token=request.headers.get('token'),
            date=utcnow(),
        )
    def get_from_state() -> dict:
        logging.debug('Getting headers from state.')
        return dict(
            browser=request.headers.user_agent,
            ip=request.session.client_ip,
            path=request.page.path,
            method='web',
            client=request.headers.client,
            latitude=request.headers.latitude,
            longitude=request.headers.longitude,
            altitude=request.headers.altitude,
            language=request.headers.language,
            token=request.headers.token,
            date=utcnow(),
        )
    logging.debug('Getting the headers of the request.')
    if isinstance(request, Request):
        return get_from_request()
    elif isinstance(request, MutableProxy):
        return get_from_state()
    else:
        return {}
