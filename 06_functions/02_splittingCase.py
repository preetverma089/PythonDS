def fetchSales():
    print("Fetching sales data...")
    # code to fetch sales data from database


def filterValidSales(sales):
    print(f"Filtering valid sales...{sales}")

def summarizeSales(sales):
    print(f"Summarizing sales data...{len(sales)}")


def generateReport(sales):
    filterValidSales(sales)
    summarizeSales(sales)

generateReport("Laptop SalesData")
