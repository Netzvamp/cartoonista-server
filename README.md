# Cartoonista example server with Flask

# Docker

https://hub.docker.com/r/rlieback/cartoonista-server

Run in background

```bash
docker-compose -p cartoonista up -d
```

or

Run Container with excluded cartoonists in Background

```bash
docker run -d -p 5000:5000 --env EXCLUDE=martin_perscheid_de,xkcd_com,islieb_de,schoenescheisse_de,explosm_net,loadingartist_com,commitstrip_com,smbc_comics_com,jamesofnotrades_com --name cartoonista-server rlieback/cartoonista-server
```
 