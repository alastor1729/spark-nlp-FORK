---
layout: model
title: Icelandic icebert_vesteinn_pipeline pipeline RoBertaEmbeddings from vesteinn
author: John Snow Labs
name: icebert_vesteinn_pipeline
date: 2024-09-05
tags: [is, open_source, pipeline, onnx]
task: Embeddings
language: is
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`icebert_vesteinn_pipeline` is a Icelandic model originally trained by vesteinn.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/icebert_vesteinn_pipeline_is_5.5.0_3.0_1725578155975.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/icebert_vesteinn_pipeline_is_5.5.0_3.0_1725578155975.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("icebert_vesteinn_pipeline", lang = "is")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("icebert_vesteinn_pipeline", lang = "is")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|icebert_vesteinn_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|is|
|Size:|296.5 MB|

## References

https://huggingface.co/vesteinn/IceBERT

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaEmbeddings