# Blockchain Signature Parser

This script is a tool I made for blockchain security research, specifically for analyzing digital signatures in the blockchain. It parses raw blockchain signatures and outputs the signatures corresponding to public keys. It also checks for any biases in the nonces used in the signatures, which can indicate potential security vulnerabilities in the blockchain. It is a useful tool for identifying potential issues in the blockchain and ensuring its overall security.

Use the ```Bash-Only``` script which is much faster than the Python version.

### Python Script (Deprecated)
This script outputs signatures corresponding to public keys from raw blockchain signatures.   

It requires the ```sponge``` tool from ```moreutils```.

**How to Use**  
-Run this command to get a folder called ```Signatures``` that contains the signatures of each corresponding public key.  ```./parseSigs.sh test.log```  

This can be tested on test.log which are raw signatures collected from the Bitcoin blockchain.  
If you want to use your own files, merely replace test.log with your file that has raw blockchain signatures.
