---
layout: model
title: English distilbert_word2vec_256k_mlm_750k_pipeline pipeline DistilBertEmbeddings from vocab-transformers
author: John Snow Labs
name: distilbert_word2vec_256k_mlm_750k_pipeline
date: 2024-09-10
tags: [en, open_source, pipeline, onnx]
task: Embeddings
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

Pretrained DistilBertEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`distilbert_word2vec_256k_mlm_750k_pipeline` is a English model originally trained by vocab-transformers.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/distilbert_word2vec_256k_mlm_750k_pipeline_en_5.5.0_3.0_1725935460879.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/distilbert_word2vec_256k_mlm_750k_pipeline_en_5.5.0_3.0_1725935460879.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("distilbert_word2vec_256k_mlm_750k_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("distilbert_word2vec_256k_mlm_750k_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|distilbert_word2vec_256k_mlm_750k_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|902.0 MB|

## References

https://huggingface.co/vocab-transformers/distilbert-word2vec_256k-MLM_750k

## Included Models

- DocumentAssembler
- TokenizerModel
- DistilBertEmbeddings