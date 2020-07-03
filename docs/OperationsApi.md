# gcloudspeechtotext.OperationsApi

All URIs are relative to *https://hackathon.tim.it/gcloudspeechtotext*

Method | HTTP request | Description
------------- | ------------- | -------------
[**speech_operations_get**](OperationsApi.md#speech_operations_get) | **GET** /v1/operations/{name} | 

# **speech_operations_get**
> Operation speech_operations_get(name, fields=fields, upload_type=upload_type, xgafv=xgafv, param_callback=param_callback, alt=alt, upload_protocol=upload_protocol, pretty_print=pretty_print, quota_user=quota_user)



Gets the latest state of a long-running operation.  Clients can use this method to poll the operation result at intervals as recommended by the API service.

### Example
```python
from __future__ import print_function
import time
import gcloudspeechtotext
from gcloudspeechtotext.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = gcloudspeechtotext.Configuration()
configuration.api_key['apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# create an instance of the API class
api_instance = gcloudspeechtotext.OperationsApi(gcloudspeechtotext.ApiClient(configuration))
name = 'name_example' # str | The name of the operation resource.
fields = 'fields_example' # str | Selector specifying which fields to include in a partial response. (optional)
upload_type = 'upload_type_example' # str | Legacy upload protocol for media (e.g. \"media\", \"multipart\"). (optional)
xgafv = 'xgafv_example' # str | V1 error format. (optional)
param_callback = 'param_callback_example' # str | JSONP (optional)
alt = 'json' # str | Data format for response. (optional) (default to json)
upload_protocol = 'upload_protocol_example' # str | Upload protocol for media (e.g. \"raw\", \"multipart\"). (optional)
pretty_print = true # bool | Returns response with indentations and line breaks. (optional) (default to true)
quota_user = 'quota_user_example' # str | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. (optional)

try:
    api_response = api_instance.speech_operations_get(name, fields=fields, upload_type=upload_type, xgafv=xgafv, param_callback=param_callback, alt=alt, upload_protocol=upload_protocol, pretty_print=pretty_print, quota_user=quota_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->speech_operations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the operation resource. | 
 **fields** | **str**| Selector specifying which fields to include in a partial response. | [optional] 
 **upload_type** | **str**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **str**| V1 error format. | [optional] 
 **param_callback** | **str**| JSONP | [optional] 
 **alt** | **str**| Data format for response. | [optional] [default to json]
 **upload_protocol** | **str**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pretty_print** | **bool**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quota_user** | **str**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

