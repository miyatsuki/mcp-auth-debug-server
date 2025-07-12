from mcp.server.fastmcp import Context, FastMCP

# Stateful server (maintains session state)
mcp = FastMCP("StatefulServer")


@mcp.tool()
def echo(message: str, ctx: Context) -> str:
    """A simple echo tool"""
    auth_header = None
    if ctx.request_context.request and hasattr(ctx.request_context.request, "headers"):
        auth_header = ctx.request_context.request.headers.get("authorization")

    return f"Echo: debug auth header {auth_header}, message: {message}"


# Run server with streamable_http transport
mcp.run(transport="streamable-http")
