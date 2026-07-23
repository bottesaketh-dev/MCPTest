import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    url = "https://mcptest-wzt4.onrender.com/mcp"
    print(f"Connecting to remote MCP server at {url}...")
    
    async with sse_client(url) as streams:
        async with ClientSession(*streams) as session:
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
