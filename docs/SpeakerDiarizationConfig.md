# SpeakerDiarizationConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_speaker_diarization** | **bool** | If &#x27;true&#x27;, enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_tag provided in the WordInfo. | [optional] 
**min_speaker_count** | **int** | Minimum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 2. | [optional] 
**max_speaker_count** | **int** | Maximum number of speakers in the conversation. This range gives you more flexibility by allowing the system to automatically determine the correct number of speakers. If not set, the default value is 6. | [optional] 
**speaker_tag** | **int** | Output only. Unused. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

