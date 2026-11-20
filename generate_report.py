from pathlib import Path

from orderlab.csv_report import largest_order_from_csv, revenue_from_csv

largest_order = largest_order_from_csv("data/sample_orders.csv")
revenue = revenue_from_csv("data/sample_orders.csv")
site = Path("site")
site.mkdir(exist_ok=True)
(site / "index.html").write_text(
    f"<h1>Orderlab Report</h1>"
    f"<p>Revenue: {revenue:,} KRW</p>"
    f"<p>Largest order: {largest_order:,} KRW</p>",
    encoding="utf-8",
)
