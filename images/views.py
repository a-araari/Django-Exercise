import uuid

from django.shortcuts import render, redirect, get_object_or_404

from .models import Image, UploadRecord
from .forms import ImageForm
from .options import get_client_ip


def upload(request):
    # to keep track of user uploaded images without authentication,
    # we use sessions app and rely on the client end.
    identifier = request.session.get('uploader_identifier', None)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)

            # if not identifier found for the current user, create a new one
            if not identifier:
                identifier = str(uuid.uuid4())
                request.session['uploader_identifier'] = identifier

            image.identifier = identifier
            image.save()

            # Get the client IP address from the request
            ip_address = get_client_ip(request)

            # Create the UploadRecord instance for the uploaded image
            UploadRecord.objects.create(ip_address=ip_address)

            return redirect('images:detail', slug=image.slug)
    else:
        form = ImageForm()

    user_images = Image.objects.filter(identifier=identifier)
    other_images = Image.objects.exclude(identifier=identifier)

    context = {
        'form': form,
        'user_images': user_images,
        'other_images': other_images
    }
    return render(request, 'images/upload.html', context=context)


def detail(request, slug):
    image = get_object_or_404(Image, slug=slug)
    is_owner = request.session.get('uploader_identifier') == str(image.identifier)

    if request.method == 'POST' and is_owner:
        image.delete()
        return redirect('images:upload')

    return render(request, 'images/details.html', context={'image': image, 'is_owner': is_owner})
