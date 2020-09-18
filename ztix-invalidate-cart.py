import requests


def get_carts():
    r = requests.get("https://api.ztix-technik.de/sale/carts/")
    return r.json()["carts"]


def invalidate_cart(cart_uuid):
    r = requests.post("https://api.ztix-technik.de/sale/carts/invalidate/", json={"cart": cart_uuid})


if __name__ == '__main__':
    carts = get_carts()
    for cart in carts:
        print("Invalidate cart ", cart["uuid"])
        invalidate_cart(cart["uuid"])
