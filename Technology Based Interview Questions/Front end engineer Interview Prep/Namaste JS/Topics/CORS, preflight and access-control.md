### CORS
Cross origin resource sharing

Initially browsers only allowed resource sharing between applications that were running on the same domain. 

A same-origin is a combination of the protocol, subdomain, domain and port. 

Example: 
http://akshaisaini.com:8080

https://... - not same origin
http://api.akshaisaini..... - not same origin
http://akshaisaini.io... - not same origin
http://akshaisaini.com:6365 - not same origin
http://akshaisaini.com:8080 - SAME ORIGIN

By enabling, `cors` we allow requests from other origins to be accepted in the application.

### Preflight
Before an API call is made , as preflight request is made, to check if the other application accepts this request or not. 

A preflight request returns some additional https headers that returned that help the current application validate if the other application is secure and a valid application to share resources with.
![[Pasted image 20231018224945.png]]

## `access-control-allow`

This is part of the options header that is returned when the preflight request is made. 

Some options are `access-control-allow-`
- `origin` - this specifies from which origins is the request accepter
- `method` - this specifies which http methods are honoured