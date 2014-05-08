from django.shortcuts import render_to_response


def home(request):
    return render_to_response("seg_mngr/index.html")

def server_manager(request):
    return render_to_response("seg_mngr/server_manager.html")
