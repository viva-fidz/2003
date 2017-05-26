$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
//        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('name');
        var product_price = submit_btn.data('price');
//        console.log( product_name,  product_price);

            var data = {};
            data.product_id = product_id;
            data.nmb = nmb;
//            console.log(nmb);
            data.nmb = parseInt(data.nmb);
//            console.log(nmb);
            var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            var url = form.attr('action');
//            console.log("data=", data);

            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data){
                    console.log('OK');
                    console.log('data.products_total_nmb=', data.products_total_nmb);
                    if (data.products_total_nmb || data.products_total_nmb == 0) {
                        $('#cart_total_nmb').text("(" + data.products_total_nmb + ")");
                         console.log(data.products)
                         $('.cart_body ul').html("");
                         $.each(data.products, function(k, v){
                             $('.cart_body ul').append('<li><a href="#">' + v.name + '</a> ' + v.nmb + ' шт ' + v.price_per_item + 'р '+
                                    '<a class="delete_item" href=""> X </a>' + '</li><br>');
                         })
                    }
                },
                error: function(){
                    console.log("error")
                }
            })
    });

    $(document).on('click', '.delete_item', function(e){
        e.preventDefault();
        $(this).closest('li').remove();
    })
   });