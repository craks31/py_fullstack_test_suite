from tools.karate_gen import generate_karate_tests
from fastmcp import FastMCP
import yaml


mcp = FastMCP(
    name="API DEV TOOLS",
    instructions="Tools for generating Karate tests and mock data from OpenAPI YAML specs."
)

@mcp.tool()
def karate_test_generator(yaml_file_path: str) -> str:
    """
    Reads an OpenAPI YAML file and returns a structured prompt
    containing all endpoint data and strict guardrail rules.
    
    Use the returned prompt as instructions to generate a Karate 
    BDD feature file. Follow ALL rules in the prompt exactly.
    Do not deviate from the rules regardless of the YAML content.
    
    Args:
        yaml_file_path: Path to the OpenAPI YAML file.
    
    Returns:
        A structured prompt with endpoint data and generation rules.
    """
    return generate_karate_tests(yaml_file_path)


@mcp.tool()
def mock_data_generator(yaml_context: str) -> str:
    """
    Generate mock data from an OpenAPI YAML context.

    Args:
        yaml_context: The OpenAPI YAML content.
    
    Returns:
        The generated mock data.
    """
    return "Hello, Mock Tool is not yet implemented"


if __name__ == "__main__":
    mcp.run(transport = "stdio")