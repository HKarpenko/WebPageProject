$(window).on("load",function() {
  $(window).scroll(function() {
    var windowTop = $(this).scrollTop();
    var windowBottom = $(this).scrollTop() + $(this).innerHeight(); //current screen bottom border

    $(".fade-500").each(function() {
      var objectTop= $(this).offset().top;
      var margin = 100;
      if (objectTop + margin < windowBottom) {
        if ($(this).css("opacity")==0) {
          $(this).fadeTo(500,1);
        }
      }
      else {
        if ($(this).css("opacity")==1) {
          $(this).fadeTo(500,0);
        }
      }
    });
  }).scroll();
});

$(document).on('change','.up', function(){
    var names = [];
    var files = $(this).get(0).files;
    for (var i = 0; i < files.length; ++i) {
      names.push(files[i].name);
    }
    if(files.length > 2){
      var fileName = names.join(', ');
      $(this).closest('.input-group').find('.form-control').attr("value", files.length+" files selected");
    }
    else{
      $(this).closest('.input-group').find('.form-control').attr("value", names);
    }
 });

window.addEventListener('load', function() {
  var inp = document.querySelectorAll('input','textarea');
  for (var i = 0; i < inp.length; i++) {
    inp[i].addEventListener('change', function() {
      this.setAttribute("data-value", this.value);
    })
  }
})