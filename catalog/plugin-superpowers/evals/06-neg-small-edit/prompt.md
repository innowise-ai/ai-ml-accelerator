---
max_turns: 5
timeout_seconds: 120
allowed_tools: [Read, Glob, Grep, Skill]
runs: 3
---
Rename `calc_total` to `compute_order_total` and update the call sites:

```python
DEFAULT_TAX = 0.2

def calc_total(items, tax_rate):
    subtotal = sum(i.price * i.qty for i in items)
    return round(subtotal * (1 + tax_rate), 2)

def checkout(cart, user):
    total = calc_total(cart.items, user.region.tax_rate)
    return charge(user, total)

def preview(cart):
    return f"Estimated: {calc_total(cart.items, DEFAULT_TAX):.2f}"

def refund_amount(order):
    return calc_total(order.returned_items, order.tax_rate)
```
