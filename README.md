# SAP Agent AI Demo MCP

This project implements a Model Context Protocol (MCP) server for a specific SAP Agent AI demo scenario.
It simulates a connection to an SAP ERP system (SD, MM, FI, PP modules) without requiring a real SAP instance.

## Features

- **Mock SAP Connector**: Simulates RFC calls and data retrieval.
- **MCP Tools**:
    - `get_sales_orders`: Query sales orders.
    - `create_sales_order`: Simulate order creation.
    - `get_purchase_orders`: Query purchase orders.
    - `check_inventory`: Check stock levels.
    - `get_account_balance`: Query financial balances.
    - `process_customer_document`: Simulate document intelligence processing.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run Local Verification
To test the tools without an MCP client:
```bash
python test_tools.py
```

### Run MCP Server
To start the MCP server (stdio mode) for use with an Agent/Client:
```bash
python server.py
```

## Configuration
The mock data logic is located in `sap_connector.py`. You can modify the `_mock_*` methods to change the returned data.
