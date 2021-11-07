from django.shortcuts import render
from chatbot2.shopping_bot import ShoppingBot
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

sb = ShoppingBot()
global x


@csrf_exempt
def index(request):
    return render(request, "index.html")


@csrf_exempt
def myajaxtestviewtext(request):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(request.POST['text'])
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    s = str(request.POST['text'])
    sb.temp = 0
    if(sb.temp > 0 or s == "checkout"):
        # print("Checking out")
        sb.temp = sb.temp + 1
        if(sb.temp == 1):
            resp = sb.handle("show list")
            resp, sb.other = resp

            sb.address = s
            flag = 0
            for product, quantity in sb.other:
                print("YO")
                p1 = Product.objects.filter(slug=product)[0]
                p = Product.objects.get(productid=p1.productid)
                cart = Cart(request)
                qty = p.quantity
                if quantity > qty:
                    resp = "Number of Items exceeded the stock..\nPlease Clear the list and try again."
                    return HttpResponse(resp)
                p.quantity = qty-quantity
                p.save()
                cart.add(product=p, quantity=quantity)
                # u = User.objects.get(username=request.user.username)
                # o = Order(item=product,quantity=quantity,price=p.price,total=(int(quantity)*int(p.price)),name=request.user.username,phone=sb.phone,email=u.email,address=sb.address,user_id=u.id)
                # o.save()
            resp = "Adding... \nCheck CART"
            sb.handle("clear list")
            sb.temp = 0
            # print(other)
        return HttpResponse(resp)
    if(s == "clear cart" or s == "empty cart"):
        cart = Cart(request)
        cart.clear()
        resp = "CLEARING CART"

        # print(other)
        return HttpResponse(resp)
    resp = sb.handle(s)

    # print(resp)

    if type(resp) is tuple:
        resp, other = resp
        print(resp)

    # print("***********************")
    if(resp == "None"):
        resp = "Done..."
    else:
        print(resp)
    # print("***********************")
    return HttpResponse(resp)
