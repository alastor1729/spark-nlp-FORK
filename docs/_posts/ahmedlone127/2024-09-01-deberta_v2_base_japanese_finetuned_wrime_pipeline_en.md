---
layout: model
title: English deberta_v2_base_japanese_finetuned_wrime_pipeline pipeline DeBertaForSequenceClassification from MuneK
author: John Snow Labs
name: deberta_v2_base_japanese_finetuned_wrime_pipeline
date: 2024-09-01
tags: [en, open_source, pipeline, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.4.2
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained DeBertaForSequenceClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`deberta_v2_base_japanese_finetuned_wrime_pipeline` is a English model originally trained by MuneK.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/deberta_v2_base_japanese_finetuned_wrime_pipeline_en_5.4.2_3.0_1725182193553.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/deberta_v2_base_japanese_finetuned_wrime_pipeline_en_5.4.2_3.0_1725182193553.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("deberta_v2_base_japanese_finetuned_wrime_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("deberta_v2_base_japanese_finetuned_wrime_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|deberta_v2_base_japanese_finetuned_wrime_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.4.2+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|421.2 MB|

## References

https://huggingface.co/MuneK/deberta-v2-base-japanese-finetuned-wrime

## Included Models

- DocumentAssembler
- TokenizerModel
- DeBertaForSequenceClassification