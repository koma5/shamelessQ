# build
```
docker build -t sendpostcard  .
```


# run
```
docker run -d --env-file secret.txt sendpostcard
```

# sample secret.txt
```
POSTUSER=post.ch user
POSTPASSWORD=
COUCHDBUSER=
COUCHDBPASSWORD=
COUCHDBURL=http://postcardsatrest:5984/postcards/
```
