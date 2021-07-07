def MaximumDiscount(n, price):
    price.sort()
    discount = 0
    if len(price) > 2:
        for i in range(2, n, 3):
            discount += price[i]
    return discount
