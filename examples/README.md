## Examples of settings runtime params
### Command-line parameters
```
app.py \
     --cream True \
     --size 16 \
     --sugar True
```
###  Environment variables
```
export CF_CREAM=True
export CF_SIZE=16
export CF_SUGAR=True
```
###  ini file
```
[settings]
cream=True
size=16
sugar=True
```
###  docker run
```
docker run -it \
     -e CF_CREAM=True \
     -e CF_SIZE=16 \
     -e CF_SUGAR=True \
     <container-name>
```
###  docker compose
```
app:
  environment:
  - CF_CREAM=True
  - CF_SIZE=16
  - CF_SUGAR=True

```
###  kubernetes
```
spec:
  containers:
  - env:
    - name: CF_CREAM
      value: 'True'
    - name: CF_SUGAR
      value: 'True'
    - name: CF_SIZE
      value: '16'
    image: ''
    name: ''

```
