function ImageRefresher() {
};

function init(inputId) {
    var that = this;
    this.inputId = '#' + inputId;
    this.imgId = '#' + inputId + '_img';
    this.origData = $(this.imgId).attr('src');
    $(this.inputId).change(function(){
        that.readURL(this);
    });
}

function readURL(input) {
    var that = this;
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $(that.imgId).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    } else {
        $(this.imgId).attr('src', this.origData);
    }
}

ImageRefresher.prototype.init = init;
ImageRefresher.prototype.readURL = readURL;

window.onload = function() {
    $('.image-preview').each(function(index) {
        var refresher = new ImageRefresher();
        refresher.init(this.id);
    });
};