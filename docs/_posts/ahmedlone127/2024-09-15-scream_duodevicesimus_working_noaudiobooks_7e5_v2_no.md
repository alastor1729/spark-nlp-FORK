---
layout: model
title: Norwegian scream_duodevicesimus_working_noaudiobooks_7e5_v2 WhisperForCTC from NbAiLabArchive
author: John Snow Labs
name: scream_duodevicesimus_working_noaudiobooks_7e5_v2
date: 2024-09-15
tags: ["no", open_source, onnx, asr, whisper]
task: Automatic Speech Recognition
language: "no"
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
engine: onnx
annotator: WhisperForCTC
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained WhisperForCTC model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`scream_duodevicesimus_working_noaudiobooks_7e5_v2` is a Norwegian model originally trained by NbAiLabArchive.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/scream_duodevicesimus_working_noaudiobooks_7e5_v2_no_5.5.0_3.0_1726410687970.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/scream_duodevicesimus_working_noaudiobooks_7e5_v2_no_5.5.0_3.0_1726410687970.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
     
audioAssembler = AudioAssembler() \
	.setInputCol("audio_content") \
	.setOutputCol("audio_assembler")

speechToText  = WhisperForCTC.pretrained("scream_duodevicesimus_working_noaudiobooks_7e5_v2","no") \
     .setInputCols(["audio_assembler"]) \
     .setOutputCol("text")

pipeline = Pipeline().setStages([audioAssembler, speechToText])
pipelineModel = pipeline.fit(data)
pipelineDF = pipelineModel.transform(data)

```
```scala

val audioAssembler = new DocumentAssembler()
    .setInputCols("audio_content")
    .setOutputCols("audio_assembler")

val speechToText = WhisperForCTC.pretrained("scream_duodevicesimus_working_noaudiobooks_7e5_v2", "no")
    .setInputCols(Array("audio_assembler")) 
    .setOutputCol("text") 
    
val pipeline = new Pipeline().setStages(Array(documentAssembler, speechToText))
val pipelineModel = pipeline.fit(data)
val pipelineDF = pipelineModel.transform(data)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|scream_duodevicesimus_working_noaudiobooks_7e5_v2|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[audio_assembler]|
|Output Labels:|[text]|
|Language:|no|
|Size:|1.7 GB|

## References

https://huggingface.co/NbAiLabArchive/scream_duodevicesimus_working_noaudiobooks_7e5_v2