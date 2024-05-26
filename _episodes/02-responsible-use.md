---
title: "Responsible Use of LLMs and Generative AI"
teaching: 15
exercises: 20
questions:
- "How do I use llms safely and responsibly?"
objectives:
- "Know when using LLMs can be a risk to privacy or IP"
- "Avoiding Errors and Consequences"
- "Reasonable use of LLMs" 
- "Strategies for Mitigating Risks" 
keypoints:
- "Depending on the LLMs product used your inputs maybe used and sensitive data maybe exposed"
- "LLMs make mistakes and they can be subtle, test, understand the consequences of a mistake"
- "Using LLMs to directly generate text can be spammy and misleading but some such uses maybe appropriate"
- "Strategies can help avoid risks"
- "LLMs can be safely used in many circumstances even where there are adjacent risks"
---

## Responsible Use of LLMs and Generative AI

As society adapts to the emergence of powerful generative AI our understanding of risks and responsible use is changing. Your use maybe need to conform to local laws or organisational policies and you should understand and work within these. Additionally broad ethical reasoning and principles can be applied. LLMs like many technologies can be used for harm. Reflect on your usage and do not use LLMs to cause harm.

### Risks to privacy and Intellecutal Property

LLMs are avaialble through a number of different outlets and policies on how data input maybe used vary. In many cases, especially where the use of the LLM is cheap, free, or through public websites, data you input may not be private. Your input data maybe used to train models or maybe accessible by the indviduals operating the LLM service. Normally companies provide terms and conditions that outline how your data will be used. In corporate settings mandated services maybe safest. For science use cases a wide variety of services might be useful. Typically your should not input Personally Identifiable Information (PII) or intellecutal property (IP) into LLMs.

In addition to the risks of supplying PII or IP into LLMs you should familiarize yourself with the terms under which you can use the outputs of LLMs. Often LLM providers allow you to use outputs for a wide variety of purposes and in some cases you may own content generated. In a few cases some LLMs are released under research only licenses and their outputs may not be used for commerical purposes. As of the time of writing openai LLMs provide liberal terms allowing many uses and ownership of outputs, further details are here https://openai.com/policies/usage-policies/. 

### Errors and consequences  

LLMs are trained to be highly reliable and in practice for many use cases they make few mistakes. However there LLMs are more likely to make mistakes on more complex tasks and these mistakes can be subtle. You should work with LLMs assuming there maybe a mistake in what the LLM outputs. Less sophisticated LLMs like ChatGPT version 3.5 are more likely to produce mistakes than better LLMs like ChatGPT 4. LLM developers generally work very hard to reduce mistakes and LLMs are often trained and tested on their ability to produce correct output.

### Disclosure

Many organisations and institutions are grappling with how to treat AI generated content. In some cases AI generated content is outright banned. In other cases AI generated content is acceptable but should be disclosed. In some cases what constitues AI Generated Content is clear. For example asking ChatGPT to generate an essay on "Common household pets" and then copying that content for direct use representing it as your own work would be deceptive and even with attribution in many cases it would not be allowed.

However what constitutes AI generated content is not always clear cut. For example you may use AI as an encyclopedia like resource to extract facts or overviews on topics (It's best to cross check facts from AIs in this case). These facts then might form the basis for your own words in an essay. Similarly AIs can be used at abstract levels to suggest research approaches, to describe suitable structures for documents or to review text and make suggestions or simple corrections. Thus AI authorship is not clear cut and disclosure or avoidance of AI content is not simple. 

As AIs become ubiquitous and predominant tools the societal attitudes to AI generated content will change and may become clearer. 

### Strategies for mitigating risk

### Testing

Testing outputs of LLMs is important. It reduces risk and it ensures that you understand the content output. Testing can take many forms. You might reason through an LLMs outputs critically assessing each of its assertions either using logic or cross checking against other material. Testing of LLM generated code might be similar to how you'd test your own code, your could write unit tests or try out the produced application, testing different usage scenarios and checking for errors.  

### Understanding consequences and setting a risk tolerance

In some cases you maybe able to tolerate some error. For example, if you are learning about trigonmetry and you are going to read a wide variety of material it maybe ok if an LLM misleads you as you will discover this error in further learning or exercises. In other cases errors could be catastrophic. For example and LLM may incorrectly analyze a series of medical documents and recommend a dangerous or incorrect treatement plan. Understanding consequences and set an appropriate risk tolerance when using LLMs.

### Censoring Data

One strategy for using LLMs with sensitive data is to generate mock data, metadata, or data structure that removes any sensitive aspects of the data. This must be approached careful as, depending on the remaining information content, some data censoring techniques can be reversed. In some cases it maybe safe to provide an LLM with column names and statistical properties of the data in the columns. LLMs can also indirectly assist in censoring data by writing scripts to generate representative datasets. For example you might ask an LLM to "Generate a python script that reads my CSV and replaces the lat and lon of each location in the location field with random lats and lons". In this example it would be still necessary to understand how the suggested script worked and whether it was sufficient to censor your data. In many cases, when direclty using LLMs, you won't want to send all the data to the LLM. Rather you maybe asking the LLM something about querying or processing your data. In that case it maybe sufficient to send the structure, e.g the column names, along with a broad description of data to the LLM.

Sensitive data in other circumstances might include things like file paths and you could remove these and substitue them with placeholders.  

### Working on Adjacent problems

Where there is a risk of exposure of intellectual property or sensitive data it still maybe possible to indirectly work with LLMs. For example you may need to learn and employ a statistical technique on your dataset. It might be possible to learn this technique and work with the LLM to generate code without any specifics of the work you are doing being provided to the LLM. Caution should be taken as over many interactions with an LLM it maybe possible for an adversary to glean information about your IP or data by looking at trends and context.  

> ## Understand terms and conditions 
>  
> Find the privacy terms and conditions for OpenAIs ChatGPT 
> 
> {: .text}
{: .challenge}


> ## Trick an LLM 
>  
>  Try to find a mistake in an LLM by asking a really tricky question at the edge of your domain knowledge?
> 
> {: .text}
{: .challenge}

> ## Examples of Sensitive Data
>  
> Write code using an LLM to generate python code that implements a basic example of conways game of life. Try executing it in the jupyterlab.
> 
> {: .text}
{: .challenge}


> ## Safe Interactions
>
>  Can you think of any safe ways of engaging an LLM around your problem when there maybe a sensitive aspect?
> 
> {: .text}
{: .challenge}

> ## Testing Results
>
> How could you test LLM output in your context?
> 
> {: .text}
{: .challenge}
