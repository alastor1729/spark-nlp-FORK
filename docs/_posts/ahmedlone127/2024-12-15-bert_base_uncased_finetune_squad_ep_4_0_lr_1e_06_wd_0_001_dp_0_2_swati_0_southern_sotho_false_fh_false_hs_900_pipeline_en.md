---
layout: model
title: English bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline pipeline BertForQuestionAnswering from danielkty22
author: John Snow Labs
name: bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline
date: 2024-12-15
tags: [en, open_source, pipeline, onnx]
task: Question Answering
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

Pretrained BertForQuestionAnswering, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline` is a English model originally trained by danielkty22.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline_en_5.5.1_3.0_1734297105443.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline_en_5.5.1_3.0_1734297105443.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

pipeline = PretrainedPipeline("bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline", lang = "en")
annotations =  pipeline.transform(df)   

```
```scala

val pipeline = new PretrainedPipeline("bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline", lang = "en")
val annotations = pipeline.transform(df)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|bert_base_uncased_finetune_squad_ep_4_0_lr_1e_06_wd_0_001_dp_0_2_swati_0_southern_sotho_false_fh_false_hs_900_pipeline|
|Type:|pipeline|
|Compatibility:|Spark NLP 5.5.1+|
|License:|Open Source|
|Edition:|Official|
|Language:|en|
|Size:|407.2 MB|

## References

https://huggingface.co/danielkty22/bert-base-uncased-finetune-squad-ep-4.0-lr-1e-06-wd-0.001-dp-0.2-ss-0-st-False-fh-False-hs-900

## Included Models

- MultiDocumentAssembler
- BertForQuestionAnswering