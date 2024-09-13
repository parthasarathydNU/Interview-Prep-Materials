![Final Diagram URL Shortening](../Images/FinalDiagramURLShortening.png)

Flow:
- Client hits DNS that is redirected to CDN, which connects to API Gateway
- API Gateway routes the request to appropriate service LB end point
- 