"""A2: last company-disclosed orders/backlog (FY2021 Q4 = Jan-Mar 2022), for context only.
Advantest stated FY21 4Q was its last disclosure of orders and backlog (A2-001), so no book-to-bill can be
computed for FY2025-FY2026. Book-to-bill here = quarterly orders / quarterly sales (company did not state one).
Inputs JPY billion from the FY2021 Q4 briefing slides.
"""
ORDERS_FY21Q4 = 199.0   # A2-003
SALES_FY21Q4 = 116.8    # A2-004
BACKLOG_FY21Q4 = 394.7  # A2-005 (31 Mar 2022)

if __name__ == "__main__":
    print(f"FY2021 Q4 (Jan-Mar 2022) orders/sales = {ORDERS_FY21Q4} / {SALES_FY21Q4} = {ORDERS_FY21Q4 / SALES_FY21Q4:.2f}")
    print(f"Backlog / quarterly sales at 31 Mar 2022 = {BACKLOG_FY21Q4 / SALES_FY21Q4:.2f} quarters of sales")
