from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

from keras_model.predict import predict

def index(request):
    return render(request, "keras_model/index.html")

def save_uploaded_image(f,name):
    with open("static/media/"+ name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def predict_Image(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image=request.FILES['image']
            save_uploaded_image(image, image._name)

            result = predict("static/media/"+ image._name)[0][1]


            resp = {'data':image._name , 'result': result}
            return render(request, "keras_model/result.html", resp)

    else:
        return render(request, "keras_model/index.html")