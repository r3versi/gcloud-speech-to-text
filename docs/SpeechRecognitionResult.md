# SpeechRecognitionResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_tag** | **int** | For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For audio_channel_count &#x3D; N, its output values can range from &#x27;1&#x27; to &#x27;N&#x27;. | [optional] 
**alternatives** | [**list[SpeechRecognitionAlternative]**](SpeechRecognitionAlternative.md) | May contain one or more recognition hypotheses (up to the maximum specified in &#x60;max_alternatives&#x60;). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

