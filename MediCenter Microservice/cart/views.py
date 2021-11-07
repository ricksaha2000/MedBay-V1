import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from products.models import Product
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.views.decorators.http import require_POST
from .cart import Cart
from orders.models import Order
from django.core.mail import send_mail
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
import json
import os
import requests
@login_required(login_url="/users/login")
def cart_add(request, product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	qty = product.quantity
	product.quantity = qty-1
	product.save()
	cart.add(product=product)
	return redirect('/shop/')

# @login_required(login_url="/users/login")
# def cart_detail(request):
# 	sub = []
# 	qty = []
# 	total = 0
# 	for key,value in request.session['cart'].items():
# 		sub.append(float(value['price']) * float(value['quantity']))
# 		qty.append(int(value['quantity']))
# 	for s in sub:
# 		total = total + s
# 	context = {
#     	'title' : 'My Cart',
#     	'sub' : sub,
#     	'total' : total
#     }
# 	return render(request,'cart/cart_detail.html',context)
@login_required(login_url="/users/login")
def cart_detail(request):
	sub = []
	qty = []
	total = 0
	if('cart' in request.session):
		for key,value in request.session['cart'].items():
			sub.append(float(value['price']) * float(value['quantity']))
			qty.append(int(value['quantity']))
		for s in sub:
			total = total + s
		context = {
			'title' : 'My Cart',
			'sub' : sub,
			'total' : total
		}
		return render(request,'cart/cart_detail.html',context)
	else:
		return redirect('/shop')

@login_required(login_url="/users/login")
def item_clear(request,product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	qty = product.quantity
	for key,value in request.session['cart'].items():
		if value['productid']==product_productid:
			product.quantity = qty+value['quantity']
			break
	product.save()
	cart.remove(product)
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def item_increment(request,product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	qty = product.quantity
	if qty>0:

		for key,value in request.session['cart'].items():
			if value['productid']==product_productid:
				product.quantity = qty-1
				break
		product.save()
		cart.add(product=product)
		return redirect('cart:cart_detail')
	else:
		messages.info(request,"No more product in the stock!")
		return redirect('cart:cart_detail')


@login_required(login_url="/users/login")
def item_decrement(request,product_productid):
	cart = Cart(request)
	product = Product.objects.get(productid=product_productid)
	qty = product.quantity
	for key,value in request.session['cart'].items():
		if value['productid']==product_productid:
			product.quantity = qty+1
			break
	cart.decrement(product=product)
	product.save()
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def cart_clear(request):
	cart = Cart(request)
	qty=[]
	pid = []
	for key,value in request.session['cart'].items():
		qty.append(value['quantity'])
		pid.append(value['productid'])
	for i in range(len(pid)):
		product = Product.objects.get(productid=pid[i])
		q = product.quantity
		product.quantity = q+qty[i]
		product.save()
	cart.clear()
	return redirect('cart:cart_detail')

@login_required(login_url="/users/login")
def checkout(request):
	sub = []
	qty = []
	total = 0
	if len(request.session['cart']) != 0:
		for key,value in request.session['cart'].items():
			sub.append(float(value['price']) * float(value['quantity']))
			qty.append(int(value['quantity']))
		for s in sub:
			total = total + s
		context = {
	    	'title' : 'CheckOut',
	    	'sub' : sub,
	    	'total' : total
	    }
		return render(request,'cart/checkout.html',context)
	else:
		messages.info(request,"Your cart Is Empty")
		return redirect('/')

@login_required(login_url="/users/login")
def confrm_checkout(request):
	if len(request.session['cart']) != 0:
		if request.method == 'POST':
			name = request.POST['name']
			phone = request.POST['phonenumber']
			email = request.POST['email']
			address = request.POST['address']
			user_id = request.user.id
			orders=[]
			tot_price=0
			tot_items = "";
			if name and phone and email and address:
				for key,value in request.session['cart'].items():
					item = value['title']
					product_id = value['productid']
					product_object = Product.objects.filter(productid = product_id)[0]
					quantity = value['quantity']
					price = value['price']
					total = (float(quantity) * float(price))
					tot_items += ', ' + str(quantity)+ ' ' + str(item)
					order = Order(item=item,
					productid=product_object ,
					quantity=quantity,
					price=price,
					total=total,
					name=name,
					phone=phone,
					email=email,
					address=address,
					user_id=user_id
					)
					order.save()
					orders.append(order)
					tot_price += order.total

				content='Hi '+request.user.username+'! Thank you for shopping with Ayurmed! '+'Your recent order with order id: '+str(order.id)+' has been successfully placed. We are prepping your order' + str(tot_items) + '. Our Team is working hard to deliver to you at the Earliest! Stay Home! Stay Safe! ~Team MedBay'
				r = requests.get(url = f"https://rapidapi.rmlconnect.net:9443/bulksms/bulksms?username=rapid-l9xh6359810000&password=617bf2eb245383001100f8a6&type=0&dlr=1&destination=917044659720&source=RMLPRD&message={content}")
				print("Status Code", r.status_code)
				# print("JSON Response ", r.json())
				send_mail("Order INVOICE", content, settings.SENDER_EMAIL, [request.user.email], fail_silently=True)
				content='Hi '+product_object.user.username+'\n\nCurrently an order with order id: '+str(order.id)+' has been successfully placed at your account.\
				Kindly, check the order and respond favourably to the customer.\n'
				send_mail("Order Alert!!", content, settings.SENDER_EMAIL, [product_object.user.email], fail_silently=True)
				# cart = Cart(request)
				# cart.clear()
				context ={
					'key': settings.STRIPE_PUBLISHABLE_KEY,
        			'orders': orders,
        			'price':int(tot_price)*100,
					'price2':tot_price
				}
				# messages.success(request,'Order Created SuccessFully')
				return render(request, 'payments/home.html', context)
			else:
				messages.info(request,'Filled All The Field')
				return redirect('cart:checkout')
		else:
			messages.warning(request,'SomeThing Went Wrong')
			return redirect('cart:checkout')
	else:
		messages.info(request,"Your cart Is Empty")
		return redirect('/')


