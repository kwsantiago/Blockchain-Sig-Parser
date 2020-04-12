# Blockchain Signature Parser
Simple Python script that parses signatures from the blockchain. 

**How to Use**  
1. First run this command to get the 10 public keys with the most corresponding signatures:  
```./parseSigs.sh test.log```
2. Then run this command to get a ```signatures.log``` file that contains all the signatures signed by a specific public key.  
```./parseSigs.sh test.log pubkey```

This can be tested on test.log which are signatures collected from the Bitcoin blockchain.  
You will notice after finishing step 2 on this test file that the public key ```047146F0E0FCB3139947CF0BEB870FE251930CA10D4545793D31033E801B5219ABF56C11A3CF3406CA590E4C14B0DAB749D20862B3ADC4709153C280C2A78BE10C``` has the most signatures signed with the same public key within this file. Use this same public key in step 2 in this manner:  
```./parseSigs.sh test.log 047146F0E0FCB3139947CF0BEB870FE251930CA10D4545793D31033E801B5219ABF56C11A3CF3406CA590E4C14B0DAB749D20862B3ADC4709153C280C2A78BE10C```
