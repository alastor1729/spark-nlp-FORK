---
layout: model
title: English lr1e4_bs16_distilbert_qa_pytorch_full_pipeline pipeline DistilBertForQuestionAnswering from tyavika
author: John Snow Labs
name: lr1e4_bs16_distilbert_qa_pytorch_full_pipeline
date: 2024-09-10
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

Pretrained DistilBertForQuestionAnswering, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`lr1e4_bs16_distilbert_qa_pytorch_full_pipeline` is a English model originally trained by tyavika.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/lr1e4_bs16_distilbert_qa_pytorch_full_pipeline_en_5.5.0_3.0_1725960467009.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/lr1e4_bs16_distilbert_qa_pytorch_full_pipeline_en_5.5.0_3.0_1725960467009.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("lr1e4_bs16_distilbert_qa_pytorch_full_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("lr1e4_bs16_distilbert_qa_pytorch_full_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|lr1e4_bs16_distilbert_qa_pytorch_full_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|247.3 MB|

## References

https://huggingface.co/tyavika/LR1E4-BS16-Distilbert-QA-Pytorch-FULL

## Included Models

- MultiDocumentAssembler
- DistilBertForQuestionAnswering