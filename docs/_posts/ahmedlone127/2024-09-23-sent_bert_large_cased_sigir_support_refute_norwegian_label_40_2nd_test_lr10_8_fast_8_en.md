---
layout: model
title: English sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8 BertSentenceEmbeddings from jojoUla
author: John Snow Labs
name: sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8
date: 2024-09-23
tags: [en, open_source, onnx, sentence_embeddings, bert]
task: Embeddings
language: en
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
engine: onnx
annotator: BertSentenceEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained BertSentenceEmbeddings model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8` is a English model originally trained by jojoUla.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8_en_5.5.0_3.0_1727113756633.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8_en_5.5.0_3.0_1727113756633.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
 
documentAssembler = DocumentAssembler() \
      .setInputCol("text") \
      .setOutputCol("document")

sentenceDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx") \
      .setInputCols(["document"]) \
      .setOutputCol("sentence")

embeddings = BertSentenceEmbeddings.pretrained("sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8","en") \
      .setInputCols(["sentence"]) \
      .setOutputCol("embeddings")       
        
pipeline = Pipeline().setStages([documentAssembler, sentenceDL, embeddings])
data = spark.createDataFrame([["I love spark-nlp"]]).toDF("text")
pipelineModel = pipeline.fit(data)
pipelineDF = pipelineModel.transform(data)

```
```scala

val documentAssembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")
    
val sentenceDL = SentenceDetectorDLModel.pretrained("sentence_detector_dl", "xx")
	.setInputCols(Array("document"))
	.setOutputCol("sentence")

val embeddings = BertSentenceEmbeddings.pretrained("sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8","en") 
    .setInputCols(Array("sentence")) 
    .setOutputCol("embeddings")

val pipeline = new Pipeline().setStages(Array(documentAssembler, sentenceDL, embeddings))
val data = Seq("I love spark-nlp").toDF("text")
val pipelineModel = pipeline.fit(data)
val pipelineDF = pipelineModel.transform(data)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|sent_bert_large_cased_sigir_support_refute_norwegian_label_40_2nd_test_lr10_8_fast_8|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[sentence]|
|Output Labels:|[embeddings]|
|Language:|en|
|Size:|1.2 GB|

## References

https://huggingface.co/jojoUla/bert-large-cased-sigir-support-refute-no-label-40-2nd-test-LR10-8-fast-8