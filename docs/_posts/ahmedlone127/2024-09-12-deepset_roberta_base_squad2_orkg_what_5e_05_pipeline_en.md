---
layout: model
title: English deepset_roberta_base_squad2_orkg_what_5e_05_pipeline pipeline RoBertaForQuestionAnswering from Moussab
author: John Snow Labs
name: deepset_roberta_base_squad2_orkg_what_5e_05_pipeline
date: 2024-09-12
tags: [en, open_source, pipeline, onnx]
task: Question Answering
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

Pretrained RoBertaForQuestionAnswering, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`deepset_roberta_base_squad2_orkg_what_5e_05_pipeline` is a English model originally trained by Moussab.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/deepset_roberta_base_squad2_orkg_what_5e_05_pipeline_en_5.5.0_3.0_1726176009038.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/deepset_roberta_base_squad2_orkg_what_5e_05_pipeline_en_5.5.0_3.0_1726176009038.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("deepset_roberta_base_squad2_orkg_what_5e_05_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("deepset_roberta_base_squad2_orkg_what_5e_05_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|deepset_roberta_base_squad2_orkg_what_5e_05_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|464.1 MB|

## References

https://huggingface.co/Moussab/deepset-roberta-base-squad2-orkg-what-5e-05

## Included Models

- MultiDocumentAssembler
- RoBertaForQuestionAnswering