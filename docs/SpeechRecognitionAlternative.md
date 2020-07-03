# SpeechRecognitionAlternative

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **float** | The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where &#x60;is_final&#x3D;true&#x60;. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating &#x60;confidence&#x60; was not set. | [optional] 
**transcript** | **str** | Transcript text representing the words that the user spoke. | [optional] 
**words** | [**list[WordInfo]**](WordInfo.md) | A list of word-specific information for each recognized word. Note: When &#x60;enable_speaker_diarization&#x60; is true, you will see all the words from the beginning of the audio. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

