While we include script tags in html, we can do it in three ways: 
-  `<script src="" />`  Html parsing is halted until script is downloaded and parsed
-  `<script src="" async />` Scripts are downloaded in parallel but HTML parsing is halted when scripts are parsed
-  `<script src="" defer />` Scripts are downloaded in parallel but script parsing happens only after HTML parsing is complete

![[Pasted image 20231018225932.png]]

## Note

- async attribute does not guarantee the order of execution of the scripts
- Defer attribute does