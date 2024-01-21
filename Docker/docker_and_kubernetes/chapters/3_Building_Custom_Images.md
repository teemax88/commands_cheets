# Building Custom Images Through Docker Server

This section includes notes from the third module, concernind custom docker images.

[Back to contents](/README.md)

### 1) Creating and using Dockerfile.

In order to create a container you should:
- Create a Dockerfile (Only with this name **without extension!**)
- Fill it with instructions. For example: 
```Dockerfile
# Use and existing docker image
FROM alpine

# Download and install a dependencies
RUN apk add --update redis

# Tell the image what to do when it starts
# As a container
CMD ["redis-server"]
```
- From the root directory execute
```bash
docker build .
```
- Wait for the building process, and for the **id** of the container
```bash
...
Step 1/3 : FROM alpine
latest: Pulling from library/alpine
...
Step 2/3 : RUN apk add --update redis
...
(1/1) Installing redis (4.0.11-r0)
...
Step 3/3 : CMD ["redis-server"]
...
Successfully built 43c796baca98
```

### 2) Custom tag for docker image

In order not to use only id to access the image, use -t flag to customize the name for your build

1) Create Docker file
2) cd to the root folder
3) Execute in console:
```
docker build -t samuraii/pyvo:latest .
```
4) Run (create+start) the image by tag:
```
docker run samuraii/pyvo[:latest] - if you add no : that the latest version will be used by default
```

### 3) Copy build context

Docker container does not know anything about the environment and stuff around. In order to move files inside the container use COPY command.

For example you want to run a node js app and have following structure:

```
.
..
Dockerfile
package.json
index.js
```

And you need to run this app with ```npm install``` and ```npm start```. So your Dockerfile should look like this:

```Dockerfile
# Specify base
FROM node:alpine

# Specify working dir for our files
WORKDIR /usr/app

# Copy build context for dependencies
COPY ./package.json ./

# Install deps
RUN npm install

# Copy all other files
COPY ./ ./

# Default command
CMD ["npm", "start"]
```

### 4 Port mapping

By default there is no port mapping from container to the outside. To map ports use: -p [local_port]:[container_port]
```
sudo docker run -p 8080:8080 samuraii/pyvo
```

### 5 Build custom Dockerfile

```
docker build -f Dockerfile.custom .
```

[Back to contents](/README.md)
