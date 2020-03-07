# image_not_found

## Error

```bash
dyld: Library not loaded: /usr/local/opt/readline/lib/libreadline.7.dylib
  Referenced from: /usr/local/bin/psql
  Reason: image not found
[1]    32507 abort      psql
```

## fix

```bash
cd /usr/local/opt/readline/lib
# ln {source} {dest}
ln libreadline.8.0.dylib libreadline.7.dylib
```

