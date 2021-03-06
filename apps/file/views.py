from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.decorators import login_required
from forms import FileUploadForm, FileDeleteForm
from models import File
from django.conf import settings
import uuid
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse

from wiki.core.plugins import registry
from wiki.plugins.macros import wiki_plugin

@login_required
def index(request):
    context = {
        'files': File.objects.all(),
    }
    for plugin in registry.get_plugins():
        print(plugin)
    return render(request, 'file.html', context)

@login_required
def upload(request):
    if request.POST:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            filename = handle_file_upload(request.FILES['file'])
            file = File.create(str(request.FILES['file']), str(filename))
            file.save()
        else:
            print("form not valid")

    return render_to_response('file.html', context_instance=RequestContext(request))

@login_required
def delete(request):
    if request.POST:
        form = FileDeleteForm(request.POST)
        if form.is_valid():
            uuid = request.POST.get('uuid', '')
            print(uuid)
            file = File.objects.filter(**{'uuid__contains': uuid}).first()
            file.delete()
            return HttpResponse(status=200)
    return HttpResponse(status=403)

def get(request, uuid):
    file = File.objects.filter(**{'uuid__contains': uuid}).first()
    if file:
        print(file)
        with open(settings.UPLOAD_PATH + str(file.filename)) as filestream:
            response = HttpResponse(FileWrapper(filestream), content_type=file.mimetype[0])
            response['Content-Disposition'] = 'attachment; filename=' + file.file
            return response
    context = {'file': file}
    return HttpResponse(status=404)

def handle_file_upload(file):
    filename = make_unique_filename()
    with open(settings.UPLOAD_PATH + str(filename), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return filename

def make_unique_filename():
    print uuid.uuid4()
    return uuid.uuid4()
