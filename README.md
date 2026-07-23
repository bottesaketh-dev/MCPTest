# Product Inventory MCP (Proof of Concept)
This is a **Model Context Protocol (MCP)** server built as a Proof of Concept (PoC) to demonstrate a paradigm shift in how we deliver value to clients.
## The Paradigm Shift
Historically, when a client asked for a way to monitor their warehouse stock, we would build a React dashboard, deploy a backend, and maintain a rigid UI. 
In the AI era, **clients don't need fixed UIs.** They have AI agents (like Claude, Antigravity, Cursor) that can interact with data dynamically.
Instead of building a frontend, we build an **MCP Endpoint**. 
This provides:
1. **Zero UI Development Cost:** No React components, CSS, or complex frontend state management.
2. **Infinite Flexibility:** The client's AI can query, summarize, and format the data exactly how they want it in that moment.
3. **Future-Proofing:** As AI agents get smarter, the client gets more value out of the same API without us having to write new features.
## What This Does
This server uses `FastMCP` (via Python) to expose a mock product inventory to an AI agent. It provides two tools:
- `search_products(query)`: Search by product name or category.
- `get_low_stock_items(threshold)`: Find items that are running low.
## How to Use This MCP

Because this is hosted on GitHub and configured as a standard Python package, it can be run **instantly** by any AI tool that supports MCP, without needing to manually clone the repository!

### Option 1: Claude Desktop

You can add this directly to your Claude Desktop `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "inventory": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/bottesaketh-dev/MCPTest.git",
        "inventory-mcp"
      ]
    }
  }
}
```

### Option 2: Running Locally (For the CTO Demo)

If you have [uv](https://docs.astral.sh/uv/) installed, you can start the server locally in one command:
```bash
uvx --from git+https://github.com/bottesaketh-dev/MCPTest.git inventory-mcp
```

Or clone and run via pip:
```bash
git clone https://github.com/bottesaketh-dev/MCPTest.git
cd MCPTest
pip install .
inventory-mcp
```