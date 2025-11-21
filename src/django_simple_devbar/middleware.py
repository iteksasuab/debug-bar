from django.conf import settings
from django.template.loader import render_to_string

class DevBarMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not getattr(settings, 'DEBUG', False):
            return response

        if not hasattr(response, 'content'):
            return response

        # Check for text/html content type
        if 'text/html' not in response.get('Content-Type', ''):
            return response

        content = response.content.decode(response.charset)
        
        # Simple injection before </body>
        if '</body>' in content:
            bar_html = render_to_string('django_simple_devbar/bar.html')
            content = content.replace('</body>', f'{bar_html}</body>')
            response.content = content.encode(response.charset)
            
            if 'Content-Length' in response:
                response['Content-Length'] = len(response.content)

        return response
