import requests
from requests.exceptions import Timeout, ConnectionError, RequestException

TARGET_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

def analyze_security_headers(target_url: str) -> dict:
    results = {                             # Initialize the results structure
    "status": "UNKNOWN",
    "error": None,
    "headers": {
        "Strict-Transport-Security": "MISSING",
        "Content-Security-Policy": "MISSING",
        "X-Frame-Options": "MISSING",
        "X-Content-Type-Options": "MISSING"
    }
    }

    try:
        # Perform HTTP GET request with timeout=5
        response = requests.get(target_url, timeout=5)
        # Check HTTP status code or proceed to inspect headers
        results["status"] = "SUCCESS"
    
        # Iterate over TARGET_HEADERS:
        #   If header in response.headers -> Mark as "PRESENT"
        #   Else -> Mark as "MISSING"
        for header in results["headers"]:
            if header in response.headers:
                results["headers"][header] = "PRESENT"
                pass
            else:
                results["headers"][header] = "MISSING"
        
    except Timeout:
        # Handle timeout specifically
        results["status"] = "FAILED"
        results["error"] = "Request timed out after 5 seconds"
    except ConnectionError:
        # Handle connection failure
        results["status"] = "FAILED"
        results["error"] = "Failed to connect to the target host"
    except RequestException as err:
        # Handle any other request-related error
        results["error"] = str(err)
        
    # Return the dictionary report
    return results

if __name__ == "__main__":
    # Test target 1: GitHub (implements strong HTTP security headers)
    target = "https://github.com"
    print(f"[*] Analyzing security headers for target: {target} ...\n")
    
    report = analyze_security_headers(target)
    
    # Print raw results dictionary
    print("--- Diagnostic Report ---")
    print(report)