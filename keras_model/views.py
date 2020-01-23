from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

from keras_model.predict import predict

def index(request):
    return render(request, "keras_model/index.html")

# Create your views here.
def predict_Image(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image=request.POST.get['image']
            result = predict(image.url)

        resp = {'data': image, 'result': result}
        return render(request, "keras_model/result.html", resp)

    else:
        return render(request, "keras_model/index.html")