import asyncio
import logging
from typing import Dict, Any, List

class SAPConnector:
    """
    Simulated SAP Connector for Demo purposes.
    Replaces real pyrfc connections with mock data returns.
    """
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)

    async def call_rfc(self, rfc_name: str, parameters: Dict) -> Dict:
        """
        Simulate an RFC call.
        """
        self.logger.info(f"Simulating RFC Call: {rfc_name} with params: {parameters}")
        await asyncio.sleep(0.5)  # Simulate network latency

        if rfc_name == "BAPI_SALESORDER_CREATEFROMDAT2":
            return self._mock_create_sales_order(parameters)
        elif rfc_name == "BAPI_MATERIAL_GET_ALL":
             return self._mock_check_inventory(parameters)
        
        return {"status": "OK", "message": f"Simulated call to {rfc_name} successful"}

    async def get_sap_data(self, module: str, query: Dict) -> Dict:
        """
        Get simulated SAP data based on module.
        """
        self.logger.info(f"Simonlating Data Fetch for Module: {module} with query: {query}")
        await asyncio.sleep(0.3)

        if module == "SD":
             return self._mock_get_sales_orders(query)
        elif module == "MM":
            return self._mock_get_purchase_orders(query)
        elif module == "FI":
            return self._mock_get_account_balance(query)
        
        return {"error": "Unknown module"}

    # --- Mock Data Helpers ---

    def _mock_get_sales_orders(self, query: Dict) -> Dict:
        customer = query.get("customer_number", "UNKNOWN")
        # In a real demo, we could filter by date, but strictly mocking happy path here
        return {
            "count": 2,
            "orders": [
                {
                    "order_id": "SO-2024001",
                    "customer": customer,
                    "date": "2024-01-15",
                    "total_value": 5000.00,
                    "currency": "CNY",
                    "status": "Completed",
                    "items": [{"material": "M-100", "qty": 10}, {"material": "M-200", "qty": 5}]
                },
                {
                    "order_id": "SO-2024005",
                    "customer": customer,
                    "date": "2024-02-01",
                    "total_value": 12000.50,
                    "currency": "CNY",
                    "status": "Processing",
                    "items": [{"material": "M-300", "qty": 20}]
                }
            ]
        }

    def _mock_create_sales_order(self, params: Dict) -> Dict:
        # Simulate successful creation
        new_id = "SO-" + str(int(params.get("customer_id", "0")[-4:]) + 90000)
        return {
            "sales_order_id": new_id,
            "status": "Created",
            "message": "Sales order created successfully"
        }

    def _mock_get_purchase_orders(self, query: Dict) -> Dict:
        vendor = query.get("vendor_number", "V-001")
        return {
            "vendor": vendor,
            "orders": [
                 {
                    "po_id": "PO-88001",
                    "date": "2024-01-10",
                    "amount": 3000,
                    "status": "Delivered"
                 },
                 {
                    "po_id": "PO-88005",
                    "date": "2024-02-02",
                    "amount": 4500,
                    "status": "Approved"
                 }
            ]
        }

    def _mock_check_inventory(self, params: Dict) -> Dict:
        material = params.get("material_number", "M-UNKNOWN")
        plant = params.get("plant", "1000")
        
        # Determine strict or random mock logic
        qty = 150 if "100" in material else 0
        
        return {
            "material": material,
            "plant": plant,
            "unrestricted_stock": qty,
            "unit": "PC",
            "storage_location": "0001"
        }

    def _mock_get_account_balance(self, query: Dict) -> Dict:
        comp_code = query.get("company_code", "1000")
        year = query.get("fiscal_year", "2024")
        return {
            "company_code": comp_code,
            "fiscal_year": year,
            "balance": 1500000.00,
            "currency": "CNY",
            "as_of_date": "2024-02-06"
        }
