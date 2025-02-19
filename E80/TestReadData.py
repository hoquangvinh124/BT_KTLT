def sort_products(products):
    for i in range(len(products)):
        for j in range(len(products)):
            pi=products[i]
            pj=products[j]
            if pi.unit_price<pj.unit_price:
                products[i]=pj
                products[j]=pi
    return products

def sort_products_desc(products):
    n = len(products)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if products[j].unit_price > products[max_idx].unit_price:
                max_idx = j
        if max_idx != i:
            products[i], products[max_idx] = products[max_idx], products[i]
    return products

