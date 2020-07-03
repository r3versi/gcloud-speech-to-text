# WordInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**word** | **str** | The word corresponding to this set of information. | [optional] 
**speaker_tag** | **int** | Output only. A distinct integer value is assigned for every speaker within the audio. This field specifies which one of those speakers was detected to have spoken this word. Value ranges from &#x27;1&#x27; to diarization_speaker_count. speaker_tag is set if enable_speaker_diarization &#x3D; &#x27;true&#x27; and only in the top alternative. | [optional] 
**end_time** | **str** | Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if &#x60;enable_word_time_offsets&#x3D;true&#x60; and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary. | [optional] 
**start_time** | **str** | Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if &#x60;enable_word_time_offsets&#x3D;true&#x60; and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

