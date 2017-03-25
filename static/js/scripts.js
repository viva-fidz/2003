$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
        $('.cart_toggled ul').append('<li><u>' + product_name + '</u>' + ' (' + nmb + 'шт.) = ' + product_price + 'руб  ' + '<a href="#" class="delete_item"> x </a>' + '</li>');
    })
});


$(document).on('click', '.delete_item', function(){
    $(this).closest('li').remove();
})
