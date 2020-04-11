# Blockchain Signature Parser
Simple Python script that parses signatures in each block to research blockchains. 

**How to Use**  
1. First run this command to get an ```output.log``` that contains all the public keys in the file:  
```python3 script.py test.log```  
2. Then use ```sort output.log | uniq -c | sort -rn | head -n 10``` to find the 10 public keys with the most signatures used of that file.  
3. Then run this command to get an ```output_withSig.log``` that contains all the signatures signed by this public key.  
```python3 script.py test.log pubkey```

This can be tested on test.log which is a bunch of signatures collected from the Bitcoin blockchain.  
You will notice after finishing step 2 on this test file that the public key ```047146F0E0FCB3139947CF0BEB870FE251930CA10D4545793D31033E801B5219ABF56C11A3CF3406CA590E4C14B0DAB749D20862B3ADC4709153C280C2A78BE10C``` has the most signatures signed with the same public key. Use this same public key in step 2 in this manner:  
```python3 script.py test.log 047146F0E0FCB3139947CF0BEB870FE251930CA10D4545793D31033E801B5219ABF56C11A3CF3406CA590E4C14B0DAB749D20862B3ADC4709153C280C2A78BE10C```
