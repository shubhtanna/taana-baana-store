import os
import secrets
import time

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

import catalog as cat

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-not-secret")
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax",
                  SESSION_COOKIE_SECURE=os.environ.get("FLASK_ENV") == "production")


def rupees(n):
    s = str(int(n))
    if len(s) > 3:
        head, tail, groups = s[:-3], s[-3:], []
        while len(head) > 2:
            groups.insert(0, head[-2:])
            head = head[:-2]
        groups.insert(0, head) if head else None
        s = ",".join(groups) + "," + tail
    return "₹" + s


app.jinja_env.filters["rupees"] = rupees


# ---------- csrf ----------

def csrf_token():
    if "csrf" not in session:
        session["csrf"] = secrets.token_urlsafe(24)
    return session["csrf"]


@app.before_request
def check_csrf():
    if request.method == "POST" and request.form.get("csrf") != session.get("csrf"):
        abort(400, "Your session expired. Please go back, refresh the page and try again.")


@app.context_processor
def globals_():
    return {"categories": cat.CATEGORIES, "csrf_token": csrf_token, "cart_count": sum(l["qty"] for l in session.get("cart", [])),
            "free_from": cat.FREE_SHIPPING_FROM}


# ---------- cart ----------

def cart_summary():
    lines = []
    for l in session.get("cart", []):
        p = cat.BY_SKU.get(l["sku"])
        if p:
            lines.append({"p": p, "size": l["size"], "qty": l["qty"], "total": p["price"] * l["qty"]})
    subtotal = sum(l["total"] for l in lines)
    shipping = 0 if not lines or subtotal >= cat.FREE_SHIPPING_FROM else cat.SHIPPING_FEE
    return {"lines": lines, "count": sum(l["qty"] for l in lines), "subtotal": subtotal, "shipping": shipping,
            "total": subtotal + shipping, "to_free": max(0, cat.FREE_SHIPPING_FROM - subtotal)}


# ---------- pages ----------

@app.get("/")
def home():
    return render_template("home.html", featured=[p for p in cat.PRODUCTS if p["featured"]])


@app.get("/collections/<slug>")
def collection(slug):
    c = cat.category(slug) or abort(404)
    products = cat.in_category(slug)
    sort = request.args.get("sort", "")
    if sort == "price":
        products = sorted(products, key=lambda p: p["price"])
    elif sort == "-price":
        products = sorted(products, key=lambda p: -p["price"])
    return render_template("collection.html", c=c, products=products, sort=sort)


@app.get("/products/<slug>")
def product(slug):
    p = cat.BY_SLUG.get(slug) or abort(404)
    related = [x for x in cat.in_category(p["category"]) if x["slug"] != slug][:4]
    return render_template("product.html", p=p, related=related, available=cat.available_sizes(p))


@app.get("/search")
def search():
    q = request.args.get("q", "").strip()
    t = q.lower()
    results = [p for p in cat.PRODUCTS if t and (t in p["name"].lower() or t in p["fabric"].lower() or t in p["category"])]
    return render_template("search.html", q=q, results=results)


@app.post("/cart/add")
def cart_add():
    p = cat.BY_SKU.get(request.form.get("sku", "")) or abort(404)
    size = request.form.get("size", "")
    if size not in cat.available_sizes(p):
        flash("Please choose a size." if not size else f"Sorry, size {size} is not available.", "error")
        return redirect(url_for("product", slug=p["slug"]))
    qty = max(1, min(5, int(request.form.get("qty") or 1)))
    lines = session.get("cart", [])
    line = next((l for l in lines if l["sku"] == p["sku"] and l["size"] == size), None)
    if line:
        line["qty"] = min(5, line["qty"] + qty)
    else:
        lines.append({"sku": p["sku"], "size": size, "qty": qty})
    session["cart"] = lines
    flash(f"Added {p['name']} ({size}) to your bag.", "ok")
    return redirect(url_for("cart"))


@app.post("/cart/update")
def cart_update():
    sku, size, qty = request.form.get("sku"), request.form.get("size"), int(request.form.get("qty") or 0)
    lines = [l for l in session.get("cart", []) if not (l["sku"] == sku and l["size"] == size)]
    if qty > 0:
        lines.append({"sku": sku, "size": size, "qty": min(5, qty)})
    session["cart"] = lines
    return redirect(url_for("cart"))


@app.get("/cart")
def cart():
    return render_template("cart.html", cart=cart_summary())


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    summary = cart_summary()
    if not summary["lines"]:
        return redirect(url_for("cart"))
    form = {k: request.form.get(k, "").strip() for k in ("name", "phone", "email", "address", "city", "pincode", "payment")}
    errors = {}
    if request.method == "POST":
        phone = "".join(ch for ch in form["phone"] if ch.isdigit())[-10:]
        if len(form["name"]) < 2:
            errors["name"] = "Please enter your name."
        if len(phone) != 10 or phone[0] not in "6789":
            errors["phone"] = "Please enter a 10-digit mobile number."
        if len(form["address"]) < 8:
            errors["address"] = "Please enter your full address."
        if not form["city"]:
            errors["city"] = "Please enter your city."
        if not (form["pincode"].isdigit() and len(form["pincode"]) == 6):
            errors["pincode"] = "Please enter a 6-digit PIN code."
        if not errors:
            number = "TB" + str(int(time.time()))[-6:]
            session["last_order"] = {"number": number, "total": summary["total"], "count": summary["count"], "city": form["city"],
                                     "payment": "UPI on delivery" if form["payment"] == "upi" else "Cash on delivery"}
            session["cart"] = []
            return redirect(url_for("order", number=number))
    return render_template("checkout.html", cart=summary, form=form, errors=errors)


@app.get("/order/<number>")
def order(number):
    o = session.get("last_order")
    if not o or o["number"] != number:
        return redirect(url_for("home"))
    return render_template("order.html", o=o)


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/shipping")
def shipping():
    return render_template("shipping.html")


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


@app.errorhandler(400)
def bad_request(e):
    return render_template("404.html", title="Something went wrong", message=e.description), 400


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
