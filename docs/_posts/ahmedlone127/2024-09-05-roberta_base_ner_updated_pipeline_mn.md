---
layout: model
title: Mongolian roberta_base_ner_updated_pipeline pipeline RoBertaForTokenClassification from Bachi06
author: John Snow Labs
name: roberta_base_ner_updated_pipeline
date: 2024-09-05
tags: [mn, open_source, pipeline, onnx]
task: Named Entity Recognition
language: mn
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForTokenClassification, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`roberta_base_ner_updated_pipeline` is a Mongolian model originally trained by Bachi06.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/roberta_base_ner_updated_pipeline_mn_5.5.0_3.0_1725512498992.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/roberta_base_ner_updated_pipeline_mn_5.5.0_3.0_1725512498992.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("roberta_base_ner_updated_pipeline", lang = "mn")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("roberta_base_ner_updated_pipeline", lang = "mn")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_base_ner_updated_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|mn|
|Size:|465.6 MB|

## References

https://huggingface.co/Bachi06/roberta-base-ner-updated

## Included Models

- DocumentAssembler
- TokenizerModel
- RoBertaForTokenClassification