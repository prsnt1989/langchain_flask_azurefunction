# langchain_flask_azurefunction
Template code to deploy langchain openai application with Flask on Azure Function

* Make sure to add following in host.json

```
"extensions": {
    "http": {
        "routePrefix": ""
    }
  },
```

