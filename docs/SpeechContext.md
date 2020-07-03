# SpeechContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phrases** | **list[str]** | A list of strings containing words and phrases \&quot;hints\&quot; so that the speech recognition is more likely to recognize them. This can be used to improve the accuracy for specific words and phrases, for example, if specific commands are typically spoken by the user. This can also be used to add additional words to the vocabulary of the recognizer. See [usage limits](https://cloud.google.com/speech-to-text/quotas#content).  List items can also be set to classes for groups of words that represent common concepts that occur in natural language. For example, rather than providing phrase hints for every month of the year, using the $MONTH class improves the likelihood of correctly transcribing audio that includes months. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

