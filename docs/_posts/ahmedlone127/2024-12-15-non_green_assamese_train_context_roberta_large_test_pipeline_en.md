---
layout: model
title: English non_green_assamese_train_context_roberta_large_test_pipeline pipeline RoBertaForSequenceClassification from kghanlon
author: John Snow Labs
name: non_green_assamese_train_context_roberta_large_test_pipeline
date: 2024-12-15
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

Pretrained RoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`non_green_assamese_train_context_roberta_large_test_pipeline` is a English model originally trained by kghanlon.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/non_green_assamese_train_context_roberta_large_test_pipeline_en_5.5.1_3.0_1734287254749.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/non_green_assamese_train_context_roberta_large_test_pipeline_en_5.5.1_3.0_1734287254749.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("non_green_assamese_train_context_roberta_large_test_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("non_green_assamese_train_context_roberta_large_test_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|non_green_assamese_train_context_roberta_large_test_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|1.3 GB|

## References

https://huggingface.co/kghanlon/non_green_as_train_context_roberta-large_TEST

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaForSequenceClassification