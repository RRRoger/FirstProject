# odoo接口返回值格式修改

#### 1. 正常odoo的标准接口返回值是下面这样的

```json
{
    "jsonrpc": "2.0",
    "id": null,
    "result": {
        "success": true
    }
}
```

#### 2. 若需按照客户的方式调整, 则此格式不满足, 调整步骤如下

##### 1. 框架代码找到`_json_response`复制出来, 修改如下

````python
def _json_response(self, result=None, error=None):
    response = {
        'jsonrpc': '2.0',
        'id': self.jsonrequest.get('id')
    }
    if error is not None:
        response['error'] = error
    if result is not None:
        response['result'] = result
        
    # Modify start ------------------------------------
    if isinstance(result, dict) and result.get('_NAKED_DATA_', False) is True:
        response = response['result']
        response.pop('_NAKED_DATA_')
    # Modify start ------------------------------------
    
    if self.jsonp:
        # If we use jsonp, that's mean we are called from another host
        # Some browser (IE and Safari) do no allow third party cookies
        # We need then to manage http sessions manually.
        response['session_id'] = self.session.sid
        mime = 'application/javascript'
        body = "%s(%s);" % (self.jsonp, json.dumps(response),)
    else:
        mime = 'application/json'
        body = json.dumps(response)

    return Response(body, headers=[('Content-Type', mime), ('Content-Length', len(body))])


JsonRequest._json_response = _json_response
````



##### 2. 接口返回时,添加一个key: `_NAKED_DATA_`,即可

```
return {
    "success": True,
    "_NAKED_DATA_": True
}
```

##### 3. 接口返回值对比



```json
// 修改前
{
    "jsonrpc": "2.0",
    "id": null,
    "result": {
        "success": true
    }
}


// 修改后
{
		"success": true
}
```

