import asyncio
import json
from server import get_sales_orders, create_sales_order, check_inventory

# This test script manually invokes the tool functions 
# to ensure the underlying logic and connector work as expected.

async def main():
    print("Testing get_sales_orders...")
    orders = await get_sales_orders("C1001", "20240101", "20240131")
    print(orders)

    print("\nTesting create_sales_order...")
    result = await create_sales_order("C1001", "M-100", 10, 99.9)
    print(result)

    print("\nTesting check_inventory...")
    stock = await check_inventory("M-100", "1000")
    print(stock)

if __name__ == "__main__":
    asyncio.run(main())
