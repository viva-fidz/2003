from django.shortcuts import render

# Create your views here.
def get_cart_form(request, product_id):
    """ Заполняет форму
    """
    if request.is_ajax():
        cart_form = CartAddProductForm(request.POST)
        context = {'form': cart_form, 'id': product_id}
        context.update(csrf(request))
        html = loader.render_to_string('cart/details.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404
