---
layout: model
title: English umberto_fine_tuned_irony_sarcasm_pipeline pipeline CamemBertForSequenceClassification from lupobricco
author: John Snow Labs
name: umberto_fine_tuned_irony_sarcasm_pipeline
date: 2024-09-05
tags: [en, open_source, pipeline, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained CamemBertForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`umberto_fine_tuned_irony_sarcasm_pipeline` is a English model originally trained by lupobricco.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/umberto_fine_tuned_irony_sarcasm_pipeline_en_5.5.0_3.0_1725544100290.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/umberto_fine_tuned_irony_sarcasm_pipeline_en_5.5.0_3.0_1725544100290.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("umberto_fine_tuned_irony_sarcasm_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("umberto_fine_tuned_irony_sarcasm_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|umberto_fine_tuned_irony_sarcasm_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|392.8 MB|

## References

https://huggingface.co/lupobricco/umBERTo_fine-tuned_irony_sarcasm

## Included Models

- DocumentAssembler
- TokenizerModel
- CamemBertForSequenceClassification