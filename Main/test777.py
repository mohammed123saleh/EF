
@allow_lazy_user
def add_to_cart(request, slug):
    item_var = []
    item = get_object_or_404(Item, slug=slug)
    order_item_qs = OrderItem.objects.filter(
        item=item,
        user=request.user,
        ordered=False
    )
    if request.method == "POST":
        try:

            key_item = list(request.POST.keys())[1]
            value_item = list(request.POST.values())[1]
            initial_price = value_item[:5] 
            the_title     = value_item[6:]
            titly = the_title.strip()
            the_price = float(initial_price)
    
        except:
            pass    

        try:        
            var = Variation.objects.get(itemy=item, Title__icontains=titly, category=key_item, pricy=the_price)           
            print(var)
            item_var.append(var)
            print(item_var)
        except:
            pass   

        for items in item_var:
            print(items.id, "محمد صالح")
            order_item_qs = order_item_qs.filter(
                item=item,
                user=request.user,
                ordered=False).filter(variation__id__exact=items,)


    if order_item_qs.exists():
        order_item = order_item_qs.first()
        order_item.quantity += 1
        order_item.save()
    else:
        order_item = OrderItem.objects.create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_item.variation.add(*item_var)
        order_item.save()

    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if not order.items.filter(item__id=order_item.id).exists():
            order.items.add(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("Main:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to cart.")
        return redirect("Main:order-summary")

