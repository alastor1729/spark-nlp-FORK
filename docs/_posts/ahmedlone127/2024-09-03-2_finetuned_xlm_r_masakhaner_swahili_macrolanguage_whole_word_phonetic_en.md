---
layout: model
title: English 2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic XlmRoBertaEmbeddings from JEdward7777
author: John Snow Labs
name: 2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic
date: 2024-09-03
tags: [en, open_source, onnx, embeddings, xlm_roberta]
task: Embeddings
language: en
edition: Spark NLP 5.5.0
spark_version: 3.0
supported: true
engine: onnx
annotator: XlmRoBertaEmbeddings
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained XlmRoBertaEmbeddings model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic` is a English model originally trained by JEdward7777.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic_en_5.5.0_3.0_1725342643497.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic_en_5.5.0_3.0_1725342643497.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python
 
documentAssembler = DocumentAssembler() \
      .setInputCol("text") \
      .setOutputCol("document")
    
tokenizer = Tokenizer() \ 
      .setInputCols("document") \ 
      .setOutputCol("token")

embeddings = XlmRoBertaEmbeddings.pretrained("2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic","en") \
      .setInputCols(["document", "token"]) \
      .setOutputCol("embeddings")       
        
pipeline = Pipeline().setStages([documentAssembler, tokenizer, embeddings])
data = spark.createDataFrame([["I love spark-nlp"]]).toDF("text")
pipelineModel = pipeline.fit(data)
pipelineDF = pipelineModel.transform(data)

```
```scala

val documentAssembler = new DocumentAssembler() 
    .setInputCol("text") 
    .setOutputCol("document")
    
val tokenizer = new Tokenizer() 
    .setInputCols(Array("document"))
    .setOutputCol("token")

val embeddings = XlmRoBertaEmbeddings.pretrained("2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic","en") 
    .setInputCols(Array("document", "token")) 
    .setOutputCol("embeddings")

val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer, embeddings))
val data = Seq("I love spark-nlp").toDF("text")
val pipelineModel = pipeline.fit(data)
val pipelineDF = pipelineModel.transform(data)

```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|2_finetuned_xlm_r_masakhaner_swahili_macrolanguage_whole_word_phonetic|
|Compatibility:|Spark NLP 5.5.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[document, token]|
|Output Labels:|[xlm_roberta]|
|Language:|en|
|Size:|1.1 GB|

## References

https://huggingface.co/JEdward7777/2-finetuned-xlm-r-masakhaner-swa-whole-word-phonetic