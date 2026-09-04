import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import Timeout, ConnectionError, RequestException

# Import the target analysis function from the module
from aethel.modules.mod_starship import analyze_security_headers


class TestStarshipModule(unittest.TestCase):
    """
    Unit test suite for mod_starship security header analysis.
    """

    @patch("requests.get")
    def test_analyze_security_headers_success(self, mock_get):
        """
        Test analysis when the target URL responds successfully with all headers present.
        """
        # Create a mock HTTP response object
        mock_response = MagicMock()
        mock_response.headers = {
            "Strict-Transport-Security": "max-age=31536000",
            "Content-Security-Policy": "default-src 'self'",
            "X-Frame-Options": "DENY",
            #"X-Content-Type-Options": "nosniff"
        }
        mock_get.return_value = mock_response

        # Execute analysis on a test URL
        result = analyze_security_headers("https://example.com")

        # Validate general status
        self.assertEqual(result["status"], "SUCCESS")
        self.assertIsNone(result["error"])

        # Validate header statuses
        for header, status in result["headers"].items():
            self.assertEqual(status, "PRESENT")

    @patch("requests.get")
    def test_analyze_security_headers_missing_headers(self, mock_get):
        """
        Test analysis when the target URL responds but misses security headers.
        """
        # Mock response with no security headers included
        mock_response = MagicMock()
        mock_response.headers = {}
        mock_get.return_value = mock_response

        result = analyze_security_headers("https://example.com")

        self.assertEqual(result["status"], "SUCCESS")
        self.assertIsNone(result["error"])

        # All target headers should be marked as MISSING
        for header, status in result["headers"].items():
            self.assertEqual(status, "MISSING")

    @patch("requests.get")
    def test_analyze_security_headers_timeout(self, mock_get):
        """
        Test handling of network timeout exception.
        """
        # Simulate a requests.exceptions.Timeout exception
        mock_get.side_effect = Timeout()

        result = analyze_security_headers("https://google.com")

        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["error"], "Request timed out after 5 seconds")

    @patch("requests.get")
    def test_analyze_security_headers_connection_error(self, mock_get):
        """
        Test handling of connection error exception.
        """
        # Simulate a requests.exceptions.ConnectionError exception
        mock_get.side_effect = ConnectionError()

        result = analyze_security_headers("https://invalid-domain.local")

        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["error"], "Failed to connect to the target host")

    @patch("requests.get")
    def test_analyze_security_headers_general_request_exception(self, mock_get):
        """
        Test handling of general RequestException errors.
        """
        # Simulate an arbitrary HTTP or request error
        mock_get.side_effect = RequestException("Generic network failure")

        result = analyze_security_headers("https://example.com")

        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["error"], "Generic network failure")
  


if __name__ == "__main__":
    unittest.main()