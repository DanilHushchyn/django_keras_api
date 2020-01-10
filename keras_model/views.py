from django.shortcuts import render
from django.http import HttpResponse


from ./predict import predict

import time

# Create your views here.
def uploadfile_server(request):
    if request.method == "POST":
        f = request.FILES.get('personico')
        baseDir = os.path.dirname(os.path.abspath(__name__))
        jpgdir = os.path.join(baseDir, 'static', 'jpg')

        filename = os.path.join(jpgdir, f.name)
        fobj = open(filename, 'wb')
        for chrunk in f.chunks():
            fobj.write(chrunk)
        fobj.close()


        #Inference Part
        start = time.monotonic()
        result = predict(filename)
        time_taken = time.monotonic() - start
        resp = {'result': result, 'time': time_taken}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    else:
        return render_to_response('uploadfile.html')