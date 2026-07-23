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
## How to Use This MCP (Zero Python Required)

To prove this to your CTO, you don't even need Python installed locally. You can deploy this server to the cloud and connect to it over HTTPS.

### 1. Cloud Deployment (1-Click)
This repository includes a `render.yaml` and `Dockerfile`. You can deploy this instantly to [Render.com](https://render.com) for free:
1. Connect your Render account to this GitHub repository.
2. Render will automatically detect the `render.yaml` and deploy it as a web service.
3. Once deployed, you will get a URL like `https://inventory-mcp.onrender.com`.

### 2. Connect Your AI (Claude Desktop / Cursor)
Once deployed, the CTO simply adds the HTTPS endpoint to their AI config. No code, no Python, just an API link:

```json
{
  "mcpServers": {
    "inventory": {
      "command": "curl",
      "args": [
        "-s",
        "https://YOUR-DEPLOYED-URL.onrender.com/mcp"
      ]
    }
  }
}
```

*Note: Since standard Claude Desktop config expects a command, we just use `curl -s` (or you can use the Antigravity SSE connection UI).*

### Alternative: Running Locally (For Development)

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