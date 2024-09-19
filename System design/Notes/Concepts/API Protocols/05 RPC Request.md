
Remote Procedure Call Request

Only two types
- XML RPC 
- JSON RPC

 Really straight forward, as they only execute a stored and well defined procedure and gets back whatever response is returned.

Examples
`request: {”method”: “my method”, “Parame”: ”[1,2,3]”, “id”: “myId”}`
` response: {”result”: “my_result”, “error”: null, “id”: “my_id”}`

#### PROS:

- The stored procedure can be written in any language and it can contain whatever code that has to be executed on that server
- This is an easier way to trigger that remotely via this RPC request
- Mainly used for internal operations where we need to do a simple operation multiple times, and we just want to set up one end point and we can call it instead of SSHing into the server to do it

Just for running remote procedures that are limited in variety