 <main>
        <div class="container">
        <div class="table-responsive text-nowrap" style="margin-top:90px">
        <h2> Order Summary</h2>
        <table class="table">
            <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Item Title</th>
                <th scope="col">Price</th>
                <th scope="col">Quantity</th>
                <th scope="col">Size</th> 
                <th scope="col">Total Item Price</th>
            </tr>
            </thead>
            <tbody>
            {% for order_item in object.items.all %}
            <tr>
                <th scope="row">{{ forloop.counter }}</th>
                <td>{{ order_item.item.title }}</td>
                <td>{{ order_item.item.price }}</td>
                <td>
                <a href="{% url 'Main:remove-single-item-from-cart' order_item.item.slug %}"><i class="fas fa-minus mr-2"></a></i>
                {{ order_item.quantity }}
                <a href="{% url 'Main:add-to-cart' order_item.item.slug %}"><i class="fas fa-plus ml-2"></a></i>
                </td>                
                <td>
                {% if order_item.variation.all %}
                {% for variation in order_item.variation.all %}
                {{ variation.title|capfirst }}
                {% endfor %}
                {% endif %}
                </td> 
                <td>
                {% if order_item.item.discount_price %}
                    $ {{ order_item.get_total_discount_item_price }}
                    <span class="badge badge-primary" style="margin-left:10px">Saving ${{ order_item.get_amount_saved }}</span>
                {% else %}
                    $ {{ order_item.get_total_item_price }}
                {% endif %}
                <a style="color:red" href="{% url 'Main:remove-from-cart' order_item.item.slug %}">
                <i class="fas fa-trash float-right"></i>
                </a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan='5'>Your Cart is Empty</td>
            </tr>
            <tr>
                <td colspan="5">
                <a class='btn btn-primary float-right ml-2'href='/'>Continue Shopping</a>
            </tr>                
            {% endfor %}
            {% if object.coupon %}
            <tr>
                <td colspan="4"><b>Coupon</b></td>
                <td><b>-${{ object.coupon.amount }}</b></td>
            </tr>            
            {% endif %}
            <tr>
                <td colspan="5"><b>Sub total</b></td>
                <td><b>${{ object.get_total }}</b></td>
            </tr>
            <tr>
                <td colspan="5">Taxes</td>
                <td>${{ object.get_taxes|floatformat:2  }}</td>
            </tr>
            {% if object.grand_total %}
            <tr>
                <td colspan="5"><b>Grand Total</b></td>
                <td><b>${{ object.grand_total|floatformat:2 }}</b></td>
            </tr>
            <tr>
                <td colspan="6">
                <a class='btn btn-primary float-right ml-2'href='/'>Continue Shopping</a>
                <a class='btn btn-warning float-right'href='/checkout/'>Proceed to Checkout</a></td>
            </tr> 
            {% endif %}                          
            </tbody>
        </table>
        </div>
        </div>
    </main>