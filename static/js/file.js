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
