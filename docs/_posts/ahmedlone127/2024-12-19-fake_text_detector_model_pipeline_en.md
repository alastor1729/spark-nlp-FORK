---
layout: model
title: English fake_text_detector_model_pipeline pipeline XlmRoBertaForSequenceClassification from TVI
author: John Snow Labs
name: fake_text_detector_model_pipeline
date: 2024-12-19
tags: [en, open_source, pipeline, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.5.1
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained XlmRoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`fake_text_detector_model_pipeline` is a English model originally trained by TVI.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/fake_text_detector_model_pipeline_en_5.5.1_3.0_1734596224184.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/fake_text_detector_model_pipeline_en_5.5.1_3.0_1734596224184.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("fake_text_detector_model_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("fake_text_detector_model_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|fake_text_detector_model_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|883.1 MB|

## References

https://huggingface.co/TVI/fake-text-detector-model

## Included Models

- DocumentAssembler
- TokenizerModel
- XlmRoBertaForSequenceClassification