$(document).ready(function(){
    var form = $('#form_buying_product');
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = parseInt(submit_btn.data('price'));
        var total_product_price = nmb * product_price;
        $('.cart_toggled ul').append('<li><u>' + product_name + '</u>' + ' (' + nmb + ' шт.) = ' + total_product_price + ' руб  ' + '<a href="#" class="delete_item"> x </a>' + '</li>');
    })
});


$(document).on('click', '.delete_item', function(){
    $(this).closest('li').remove();})

//$(document).ready(function() {
//
//    $( "cart_top img" ).click(function(){
//        var toLoad = $(this).'#cart_header';
//           $('#cart_header').load(toLoad);
//        //alert('continue?');
//        alert($(this).attr('href').length-5);
//        window.location.hash = $(this).attr('href').substr(0,$(this).attr('href').length-5);
//        return false; // чтобы не переходить на новую страницу
//    });
//});
