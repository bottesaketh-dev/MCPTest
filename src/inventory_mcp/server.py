from mcp.server.fastmcp import FastMCP
# Create a FastMCP server
mcp = FastMCP("inventory-mcp")
# Mock database
INVENTORY = [
    {"id": "p1", "name": "Wireless Mouse", "category": "Electronics", "stock": 45, "price": 29.99},
    {"id": "p2", "name": "Mechanical Keyboard", "category": "Electronics", "stock": 8, "price": 149.99},
    {"id": "p3", "name": "Standing Desk", "category": "Furniture", "stock": 2, "price": 499.00},
    {"id": "p4", "name": "Ergonomic Chair", "category": "Furniture", "stock": 15, "price": 250.00},
    {"id": "p5", "name": "USB-C Hub", "category": "Accessories", "stock": 102, "price": 45.00},
    {"id": "p6", "name": "Noise Cancelling Headphones", "category": "Electronics", "stock": 5, "price": 349.99},
    {"id": "p7", "name": "Webcam 1080p", "category": "Electronics", "stock": 0, "price": 59.99},
    {"id": "p8", "name": "Mousepad", "category": "Accessories", "stock": 200, "price": 12.99},
]
@mcp.tool()
def search_products(query: str) -> list[dict]:
    """Search for products in the inventory by name or category."""
    query = query.lower()
    return [
        item for item in INVENTORY
        if query in item["name"].lower() or query in item["category"].lower()
    ]
@mcp.tool()
def get_low_stock_items(threshold: int = 10) -> list[dict]:
    """Get a list of products that have a stock level equal to or below the threshold."""
    return [
        item for item in INVENTORY
        if item["stock"] <= threshold
    ]
def main():
    import os
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    if transport == "sse":
        port = int(os.getenv("PORT", "8000"))
        mcp.settings.port = port
        mcp.settings.host = "0.0.0.0"
        print(f"Starting SSE server on port {port}...", flush=True)
        mcp.run(transport="sse")
    else:
        mcp.run()

if __name__ == "__main__":
    main()
