FROM python:3.12-slim

WORKDIR /app
COPY . /app/

RUN pip install --no-cache-dir .

ENV MCP_TRANSPORT=sse
ENV PORT=8000
EXPOSE 8000

CMD ["inventory-mcp"]
