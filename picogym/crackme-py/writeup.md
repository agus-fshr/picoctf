# CrackMe-py

## First Look

Opening the `crackme.py` file reveals two functions `choose_greatest()` and `decode_secret()`. This last one is interesting, especially when you find the variable named `bezos_cc_secret`. Perhaps this functio can be used to decode that. It can. Eexcuting `decode_secret(bezos_cc_secret)` will reveal the flag for this challenge.