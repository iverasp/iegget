// reload page when dropzone completes uploading all files

Dropzone.options.dropzoneForm = {
  init: function() {
    this.on("complete", function(file) {
      if (this.getUploadingFiles().length === 0 && this.getQueuedFiles().length === 0) {
            location.reload();
        }
    });
  }
}

// get csrftoken from cookie and place in header
// from https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/#ajax

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function remove_file(elem, uuid) {
  console.log(uuid);
  $.ajax({
    method: "POST",
    url: '/file/delete/',
    data: {
      'uuid': uuid,
    }
  })
  .done(function() {
    elem.remove();
  })
  .fail(function() {
    console.log("failed to delete file");
  })
}
