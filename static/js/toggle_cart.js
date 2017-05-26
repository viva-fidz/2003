$(document).ready(function(){

    $('#cart').on('click', function(e){
        e.preventDefault();
        $('.cart_toggled').toggleClass('hidden');
    })
    $('#cart').mouseover(function(){
        $('.cart_toggled').removeClass('hidden');
    })
//    $('#cart').mouseout(function(){
//        $('.cart_toggled').addClass('hidden');
//    })
});



$(document).ready(function() {
    var stickyNavTop = $('.nav').offset().top;

    var stickyNav = function(){
    var scrollTop = $(window).scrollTop();

    if (scrollTop > stickyNavTop) {
        $('.nav').addClass('sticky');
    } else {
        $('.nav').removeClass('sticky');
    }
    };

    stickyNav();

    $(window).scroll(function() {
      stickyNav();
    });
});


//Фильтры

$(document).ready(function(){

    $('#f_price').on('click', function(e){
        e.preventDefault();
        $('.filter_price').removeClass('hidden');
        $('.filter_category').addClass('hidden');
        $('.filter_name').addClass('hidden');

    })

    $('#f_name').on('click', function(e){
        e.preventDefault();
        $('.filter_name').removeClass('hidden');
        $('.filter_category').addClass('hidden');
        $('.filter_price').addClass('hidden');

    })
});
