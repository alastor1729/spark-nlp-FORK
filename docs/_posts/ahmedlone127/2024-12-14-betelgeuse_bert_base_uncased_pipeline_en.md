---
layout: model
title: English betelgeuse_bert_base_uncased_pipeline pipeline BertEmbeddings from prithivMLmods
author: John Snow Labs
name: betelgeuse_bert_base_uncased_pipeline
date: 2024-12-14
tags: [en, open_source, pipeline, onnx]
task: Embeddings
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

Pretrained BertEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`betelgeuse_bert_base_uncased_pipeline` is a English model originally trained by prithivMLmods.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/betelgeuse_bert_base_uncased_pipeline_en_5.5.1_3.0_1734220665201.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/betelgeuse_bert_base_uncased_pipeline_en_5.5.1_3.0_1734220665201.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("betelgeuse_bert_base_uncased_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("betelgeuse_bert_base_uncased_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|betelgeuse_bert_base_uncased_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|407.2 MB|

## References

https://huggingface.co/prithivMLmods/Betelgeuse-bert-base-uncased

## Included Models

- DocumentAssembler
- TokenizerModel
- BertEmbeddings