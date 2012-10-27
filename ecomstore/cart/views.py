from django.shortcuts import render_to_response
from ecomstore.cart import cart
from django.template import RequestContext


def show_cart(request, template_name="cart/cart.html"):
    
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))
