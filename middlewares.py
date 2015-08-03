from django.shortcuts import redirect


class CustomAuthMiddleware:
    @staticmethod
    def process_request(request):
        if request.user.is_authenticated():
            pass
        else:
            return redirect('index')
