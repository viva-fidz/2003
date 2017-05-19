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

