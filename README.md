# langchain_flask_azurefunction
Template code to deploy langchain openai application with Flask on Azure Function

* Pre-requisits : VS-code, Azure Tool Extension, Azure Sign-in

* Step-1 : With in Local Projects create a Function -> Select Main Folder -> Python -> Python Interpreter -> HTTPS trigger -> {NAME} -> Anonymous

* Step-2 : Clone this Repository in the same Main folder (Or Copy files in the folder created)

* Step-3 : Make sure to add following in host.json

```
"extensions": {
    "http": {
        "routePrefix": ""
    }
  },
```

* Step-4 : Also add following in the requirements

```
langchain
openai
faiss-cpu
tiktoken
Flask
requests
```
