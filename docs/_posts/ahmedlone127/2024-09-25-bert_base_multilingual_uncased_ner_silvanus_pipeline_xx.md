---
layout: model
title: Multilingual bert_base_multilingual_uncased_ner_silvanus_pipeline pipeline BertForTokenClassification from rollerhafeezh-amikom
author: John Snow Labs
name: bert_base_multilingual_uncased_ner_silvanus_pipeline
date: 2024-09-25
tags: [xx, open_source, pipeline, onnx]
task: Named Entity Recognition
language: xx
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained BertForTokenClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`bert_base_multilingual_uncased_ner_silvanus_pipeline` is a Multilingual model originally trained by rollerhafeezh-amikom.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_multilingual_uncased_ner_silvanus_pipeline_xx_5.5.0_3.0_1727247866149.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/bert_base_multilingual_uncased_ner_silvanus_pipeline_xx_5.5.0_3.0_1727247866149.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("bert_base_multilingual_uncased_ner_silvanus_pipeline", lang = "xx")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("bert_base_multilingual_uncased_ner_silvanus_pipeline", lang = "xx")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_base_multilingual_uncased_ner_silvanus_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|xx|
|Size:|625.6 MB|

## References

https://huggingface.co/rollerhafeezh-amikom/bert-base-multilingual-uncased-ner-silvanus

## Included Models

- DocumentAssembler
- TokenizerModel
- BertForTokenClassification