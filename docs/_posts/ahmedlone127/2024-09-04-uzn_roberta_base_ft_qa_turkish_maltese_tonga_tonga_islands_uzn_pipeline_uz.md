---
layout: model
title: Uzbek uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline pipeline RoBertaForQuestionAnswering from med-alex
author: John Snow Labs
name: uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline
date: 2024-09-04
tags: [uz, open_source, pipeline, onnx]
task: Question Answering
language: uz
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
annotator: PipelineModel
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForQuestionAnswering, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline` is a Uzbek model originally trained by med-alex.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline_uz_5.5.0_3.0_1725478894582.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline_uz_5.5.0_3.0_1725478894582.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline", lang = "uz")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline", lang = "uz")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|uzn_roberta_base_ft_qa_turkish_maltese_tonga_tonga_islands_uzn_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Language:|uz|
|Size:|311.9 MB|

## References

https://huggingface.co/med-alex/uzn-roberta-base-ft-qa-tr-mt-to-uzn

## Included Models

- MultiDocumentAssembler
- RoBertaForQuestionAnswering