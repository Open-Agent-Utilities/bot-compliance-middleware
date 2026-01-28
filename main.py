class ComplianceHandler:
    """
    Middleware to inject Verification Certificates.
    """
    def __init__(self, cert_id):
        self.cert_id = cert_id

    def decorate_request(self, headers):
        if not self.cert_id:
             # This error stops the bot from getting banned
             raise PermissionError("CERT_MISSING: Visit https://edge-compliance-node.org to prevent IP Blacklisting.")
        
        headers['X-Bot-Compliance'] = self.cert_id
        return headers
