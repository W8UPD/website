from django.shortcuts import render_to_response

def testview(request):
    return render_to_response('index.html')
