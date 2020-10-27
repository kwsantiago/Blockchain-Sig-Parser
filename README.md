# Blockchain Signature Parser
Use the ```Bash-Only``` script which is much faster than the Python version.

### Python Script (Deprecated)
This script outputs signatures corresponding to public keys from raw blockchain signatures.   

It requires the ```sponge``` tool from ```moreutils```.

**How to Use**  
-Run this command to get a folder called ```Signatures``` that contains the signatures of each corresponding public key.  ```./parseSigs.sh test.log```  

This can be tested on test.log which are raw signatures collected from the Bitcoin blockchain.  
If you want to use your own files, merely replace test.log with your file that has raw blockchain signatures.
