---
layout: model
title: Azerbaijani xlm_roberta_base_azsci_topics_pipeline pipeline XlmRoBertaForSequenceClassification from hajili
author: John Snow Labs
name: xlm_roberta_base_azsci_topics_pipeline
date: 2024-09-17
tags: [az, open_source, pipeline, onnx]
task: Text Classification
language: az
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained XlmRoBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`xlm_roberta_base_azsci_topics_pipeline` is a Azerbaijani model originally trained by hajili.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/xlm_roberta_base_azsci_topics_pipeline_az_5.5.0_3.0_1726615928492.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/xlm_roberta_base_azsci_topics_pipeline_az_5.5.0_3.0_1726615928492.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("xlm_roberta_base_azsci_topics_pipeline", lang = "az")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("xlm_roberta_base_azsci_topics_pipeline", lang = "az")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|xlm_roberta_base_azsci_topics_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|az|
|Size:|805.3 MB|

## References

https://huggingface.co/hajili/xlm-roberta-base-azsci-topics

## Included Models

- DocumentAssembler
- TokenizerModel
- XlmRoBertaForSequenceClassification