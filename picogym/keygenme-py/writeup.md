# `keygenme-py`
## Download the file
We can download the file to this level by doing `wget https://mercury.picoctf.net/static/0c363291c47477642c72630d68936e50/keygenme-trial.py`.

## Open it
Open the file in your favorite text editor. For me, this is neovim, so I'll do `nvim keygenme-trial.py`.

## Read the code
If you read the code it's easy to see it'll run a small menu and lock certain features behind a trial version. Naturally, to access the full version it asks for a license. Of course, it'll have to check if this key is valid, that would be in `check_key()`. The first bit of the key is easy to find. It's in the first lines around `key_part_static1_trial`. For the next part, we'll get into `check_key()`.

There are a bunch of `if` statements in this function that are here solely to check the characters of the entered key at certain indices and compares them to the characters at certain positions of `hashlib.sha256(username_trial).hexdigest()`. This is great progress. Now all we need to is find `username_trial` and get those characters. That would look something like this.

```python

import hashlib

# strings must be encoded before hashing
s = b"MORTON"
l = [4,5,3,6,2,7,1,8]

key = "picoCTF{1n_7h3_|<3y_of_"

for i in l:
  key += hashlib.sha256(s).hexdigest()[i]

key += "}"

print(key)
```
