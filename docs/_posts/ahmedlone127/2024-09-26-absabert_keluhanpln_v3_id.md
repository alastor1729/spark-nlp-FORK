---
layout: model
title: Indonesian absabert_keluhanpln_v3 BertForSequenceClassification from radityapranata
author: John Snow Labs
name: absabert_keluhanpln_v3
date: 2024-09-26
tags: [id, open_source, onnx, sequence_classification, bert]
task: Text Classification
language: id
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
engine: onnx
annotator: BertForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained BertForSequenceClassification model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`absabert_keluhanpln_v3` is a Indonesian model originally trained by radityapranata.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/absabert_keluhanpln_v3_id_5.5.0_3.0_1727364190803.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/absabert_keluhanpln_v3_id_5.5.0_3.0_1727364190803.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
     
documentAssembler = DocumentAssembler() \
    .setInputCol('text') \
    .setOutputCol('document')
    
tokenizer = Tokenizer() \
    .setInputCols(['document']) \
    .setOutputCol('token')

sequenceClassifier  = BertForSequenceClassification.pretrained("absabert_keluhanpln_v3","id") \
     .setInputCols(["documents","token"]) \
     .setOutputCol("class")

pipeline = Pipeline().setStages([documentAssembler, tokenizer, sequenceClassifier])
data = spark.createDataFrame([["I love spark-nlp"]]).toDF("text")
pipelineModel = pipeline.fit(data)
pipelineDF = pipelineModel.transform(data)

```
```scala

val documentAssembler = new DocumentAssembler()
    .setInputCols("text")
    .setOutputCols("document")
    
val tokenizer = new Tokenizer()
    .setInputCols(Array("document"))
    .setOutputCol("token")

val sequenceClassifier = BertForSequenceClassification.pretrained("absabert_keluhanpln_v3", "id")
    .setInputCols(Array("documents","token")) 
    .setOutputCol("class") 
    
val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer, sequenceClassifier))
val data = Seq("I love spark-nlp").toDS.toDF("text")
val pipelineModel = pipeline.fit(data)
val pipelineDF = pipelineModel.transform(data)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|absabert_keluhanpln_v3|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[class]|
|Language:|id|
|Size:|409.4 MB|

## References

https://huggingface.co/radityapranata/absabert-keluhanpln-v3