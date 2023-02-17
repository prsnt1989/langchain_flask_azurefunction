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
* Step-5 : Click F5 -> This will start installing all the requirements and run the code if you see the bottom bar of the VS-code turn orange without any error in the Terminal. You are good to deploy the function.

* Step-6 : Go to Azure in VS-code and click on the function you just created -> Select Function App (If you have not created one yet. You can do that in azure portal or in vs-code itself)-> and click on the deploy symbol. Click deploy on the pop-up again.

* Step-6 : Once you see the prompt that deployment is completed. Go to the portal -> Function App -> Select the Function App in which you deployed the function -> Functions -> Click on the name of the Function -> Get Function Uri -> Open the Uri with-out any route
