from mcp.server.fastmcp import FastMCP
from .sap_connector import SAPConnector
import asyncio
import json

# Initialize the Mock SAP Connector
sap_config = {
    "ashost": "mock_host",
    "sysnr": "00",
    "client": "100",
    "user": "demo",
    "passwd": "demo",
    "lang": "ZH"
}
connector = SAPConnector(sap_config)

# Create an MCP Server
mcp = FastMCP("SAP Agent AI Demo")

@mcp.tool()
async def get_sales_orders(customer_number: str, date_from: str = None, date_to: str = None) -> str:
    """
    Get sales orders list for a customer.
    Args:
        customer_number: The SAP customer number (e.g., C1001)
        date_from: Start date (YYYYMMDD)
        date_to: End date (YYYYMMDD)
    """
    query = {
        "customer_number": customer_number,
        "date_from": date_from,
        "date_to": date_to
    }
    result = await connector.get_sap_data("SD", query)
    return json.dumps(result, ensure_ascii=False, indent=2)

@mcp.tool()
async def create_sales_order(customer_id: str, material_number: str, quantity: int, price: float) -> str:
    """
    Create a new sales order.
    Args:
        customer_id: Customer ID
        material_number: Material SKU
        quantity: Order quantity
        price: Unit price
    """
    params = {
        "customer_id": customer_id,
        "material_number": material_number,
        "quantity": quantity,
        "price": price
    }
    # Simulate Calling BAPI_SALESORDER_CREATEFROMDAT2
    result = await connector.call_rfc("BAPI_SALESORDER_CREATEFROMDAT2", params)
    return json.dumps(result, ensure_ascii=False, indent=2)

@mcp.tool()
async def get_purchase_orders(vendor_number: str, status: str = None) -> str:
    """
    Get purchase orders for a vendor.
    """
    query = {"vendor_number": vendor_number, "status": status}
    result = await connector.get_sap_data("MM", query)
    return json.dumps(result, ensure_ascii=False, indent=2)

@mcp.tool()
async def check_inventory(material_number: str, plant: str) -> str:
    """
    Check inventory stock for a material at a specific plant.
    """
    params = {"material_number": material_number, "plant": plant}
    result = await connector.call_rfc("BAPI_MATERIAL_GET_ALL", params)
    return json.dumps(result, ensure_ascii=False, indent=2)

@mcp.tool()
async def get_account_balance(company_code: str, fiscal_year: str) -> str:
    """
    Get G/L account balance for a company.
    """
    query = {"company_code": company_code, "fiscal_year": fiscal_year}
    result = await connector.get_sap_data("FI", query)
    return json.dumps(result, ensure_ascii=False, indent=2)

@mcp.tool()
async def process_customer_document(document_type: str, document_content: str, customer_id: str) -> str:
    """
    Simulate processing a document (OCR/Intelligence) and converting to SAP data.
    """
    # Mock Document Intelligence Logic
    processed_data = {
        "extracted_fields": {
            "customer_number": customer_id,
            "document_type": document_type,
            "amount": "15000.00", 
            "date": "2024-02-06",
            "content_snippet": document_content[:50] + "..."
        },
        "confidence": 0.98,
        "sap_ready_data": {
            "header": {"doc_type": "DR", "comp_code": "1000"},
            "items": [{"item": 10, "amount": 15000.00}]
        }
    }
    return json.dumps(processed_data, ensure_ascii=False, indent=2)

def main():
    import sys
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
