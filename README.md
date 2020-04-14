# Blockchain Signature Parser
This script outputs signatures corresponding to public keys from raw blockchain signatures.  

-Edit the parseSigs.sh file for certain parameters you might want, such as minumum and maximum signatures for a public key to have, or for a certain amount of public keys to be displayed.  

**How to Use**  
-Run this command to get a folder called ```Signatures``` that contains the signatures of each corresponding public key.  ```./parseSigs.sh test.log```  

This can be tested on test.log which are raw signatures collected from the Bitcoin blockchain.  
If you want to use your own files, 
merely replace test.log with your file that has raw blockchain signatures.


