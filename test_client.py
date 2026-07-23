import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Define the parameters to run our MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["src/inventory_mcp/server.py"]
    )

    print("Starting MCP server...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            print("Connected successfully!")
            
            # List available tools
            tools = await session.list_tools()
            print("\nAvailable Tools:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")
            
            # Test calling the get_low_stock_items tool
            print("\nTesting 'get_low_stock_items' tool with threshold=10...")
            result = await session.call_tool("get_low_stock_items", {"threshold": 10})
            
            print("\nResult from MCP Server:")
            print(result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
