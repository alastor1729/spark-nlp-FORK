---
layout: model
title: English bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline pipeline BertEmbeddings from iMahdiGhazavi
author: John Snow Labs
name: bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline
date: 2024-09-24
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

Pretrained BertEmbeddings, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline` is a English model originally trained by iMahdiGhazavi.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline_en_5.5.0_3.0_1727161796011.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline_en_5.5.0_3.0_1727161796011.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_persian_farsi_base_uncased_nlp_course_hw2_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|605.8 MB|

## References

https://huggingface.co/iMahdiGhazavi/bert-fa-base-uncased-nlp-course-hw2

## Included Models

- DocumentAssembler
- TokenizerModel
- BertEmbeddings