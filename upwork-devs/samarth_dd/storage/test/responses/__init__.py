import os

from scrapy.http import Response, Request, TextResponse


def fake_response_from_file(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the responses directory,
                      but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.
    """
    if not url:
        url = 'http://www.google.com'

    request = Request(url=url)
    if not file_name[0] == '/':
        responses_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(responses_dir, file_name)
    else:
        file_path = file_name

    file_content = open(file_path, 'r').read()

    response = Response(url=url,
        request=request,
        body=file_content)
    response.encoding = 'utf-8'
    return response

def fake_response(file_name=None, url=None):
    """Create a Scrapy fake HTTP response from a HTML file"""
    response=''
    if not url:
        url = 'http://www.example.com'
        request = Request(url=url)
    if file_name:
        if not file_name[0] == '/':
            responses_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(responses_dir, file_name)
        else:
            file_path = file_name
            file_content = open(file_path, 'r').read()
    else:
        file_content = ''
        response = TextResponse(url=url, request=request, body=file_content,
        encoding='utf-8')
    return response