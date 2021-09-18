# fluffy-api
Python API to receive and store pictures


***

### Setup steps


#### MacOS
1. Install python-pyodbc (maybe?)
> brew update
> 
> brew install unixodbc freetds python-pyodbc
2. Use config_default.yaml as template for your SQL configurations.  Copy and place in:
>~/.config/fluffy-api/config.yaml
3. . 

***

### Testing 

#### Test POST 
> curl -i -H 'x-api-key: &lt;INSERT API KEY HERE&gt;' -F "image=@/path/to/image.png" http://localhost:5000/Upload/

