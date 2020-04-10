# Blockchain Signature Parser
Simple Python script that parses signatures in each block to research blockchains. 

**How to Use**  
For a general file:  
```python3 script.py file.log```  
To search for signatures for one specific public key:  
```python3 script.py file.log pubkey```

Use ```sort test.txt | uniq -c | sort -rn | head -n 10``` to find the 10 top public keys with the most signatures used after running ```python3 script.py file.log```. Then run the second script to output those signatures to a seprate file.

