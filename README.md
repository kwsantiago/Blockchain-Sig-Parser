# Blockchain Signature Parser
Simple Python script that parses signatures in each block to research blockchains. 

**How to Use**  
1. First run this command to get an ```output.log``` that contains all the public keys in the file:  
```python3 script.py file.log```  
2. Then use ```sort output.log | uniq -c | sort -rn | head -n 10``` to find the 10 public keys with the most signatures used of that file.  
3. Then run this command to get an ```output_withSig.log``` that contains all the signatures signed by this public key.  
```python3 script.py file.log pubkey```

