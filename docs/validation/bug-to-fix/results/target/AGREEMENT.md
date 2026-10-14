# Synthetic pricing agreement
R1: Discount is a fraction of subtotal: [40, 60] at .10 returns 90.
R2: Zero discount returns subtotal; empty prices return zero, including at .10.
D1: Display a total of 90 as "Total: 90.00". This direct change is separate from R1/R2.
Keep the total(prices, discount) signature and caller fraction units.
No currency/rounding semantics, invalid-input contract, tax, persistence or API redesign.
Python arithmetic fixture only; no real customer/payment integration.
