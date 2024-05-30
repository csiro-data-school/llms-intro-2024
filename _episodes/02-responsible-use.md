---
title: "Responsible Use of Generative AI"
teaching: 15
exercises: 20
questions:
- "How do I use Generative AI safely and responsibly?"
objectives:
- "Recognize the ethical risks and legal restrictions using LLMs and adopted a considreed approach"
- "Identify risks to privacy and intellectual property when using LLMs"
- "Understand errors and their consequences"
- "Develop strategies for risk mitigation"

keypoints:
- "Your inputs may be used, and sensitive data may be exposed depending on the LLM product used."
- "LLMs make mistakes that can be subtle; always test and understand the consequences."
- "Directly generating text with LLMs can be spammy and misleading, but some uses may be appropriate."
- "Effective strategies can help avoid risks."
- "LLMs can be safely used in many circumstances even where there are adjacent risks."
---

## Responsible Use of LLMs and Generative AI

As society adapts to the emergence of powerful generative AI, our understanding of risks and responsible use is changing. Use may need to conform to local laws or organizational policies. Additionally, broad ethical reasoning and principles can be applied. LLMs, like many technologies, can be used for harm. Reflect on usage and do not use LLMs to cause harm.

There are many emerging policies and frameworks that are useful for reference, such as [Australia’s AI Ethics Principles](https://www.industry.gov.au/publications/australias-artificial-intelligence-ethics-framework/australias-ai-ethics-principles) and [Artificial Intelligence Safety Institute Consortium](https://www.nist.gov/aisi/artificial-intelligence-safety-institute-consortium-aisic). 

### Risks to Privacy and Intellectual Property

LLMs are available through a number of different outlets, and policies on how input data may be used vary. In many cases, especially where the use of the LLM is cheap, free, or through public websites, data input may not be private. Input data may be used to train models or may be accessible by the individuals operating the LLM service. Companies usually provide terms and conditions that outline how data will be used. In corporate settings, mandated services may be safest. For science use cases, a wide variety of services might be useful. Extra caution should be used when determining whether Personally Identifiable Information (PII) or intellectual property (IP) should be input into LLMs, in many cases this would not be safe and likley violate ethics and policy.

#### Output use restrictions

In addition to the risks of supplying PII or IP into LLMs, you should familiarize yourself with the terms under which you can use the outputs of LLMs. Often, LLM providers allow you to use outputs for a wide variety of purposes, and in some cases, you may own the content generated. Some LLMs are released under research-only licenses, and their outputs may not be used for commercial purposes. As of the time of writing, OpenAI LLMs provide liberal terms allowing many uses and ownership of outputs. Further details are available [here](https://openai.com/policies/usage-policies/). 

### Biases, Errors and Consequences  

LLMs are trained to be highly reliable and in practice, for many use cases, they make few mistakes. Similarly most LLM providers put a signficiant amount of work into "algining" LLMs to reduce biases and risks related to unethical outputs. Nevertheless, LLMs can make mistakes or display biases. 

LLMs are more likely to make mistakes on more complex tasks, and these mistakes can be subtle. You should work with LLMs assuming there may be a mistake or bias in what the LLM outputs. Less sophisticated LLMs like ChatGPT version 3.5 are more likely to produce mistakes than better LLMs like ChatGPT 4. 

### Disclosure

Many organizations and institutions are grappling with how to treat AI-generated content. In some cases, AI-generated content is outright banned. In other cases, AI-generated content is acceptable but should be disclosed. In some cases, what constitutes AI-generated content is clear. For example, asking ChatGPT to generate an essay on "Common household pets" and then copying that content for direct use, representing it as your own work, would be deceptive and even with attribution, in many cases, it would not be allowed. 

#### What consitutes AI generated content? 

However, what constitutes AI-generated content is not always clear cut. For example, AI maybe used as an encyclopedia-like resource to extract facts or overviews on topics (it's best to cross-check facts from AIs in this case). These facts then might form the basis for original work in an essay. Similarly, AIs can be used at abstract levels to suggest research approaches, describe suitable structures for documents, or review text and make suggestions or simple corrections. Thus, AI authorship is not clear cut, and disclosure or avoidance of AI content is not simple. 

#### Adding Value

One guiding principle when working with generative AI might be to ask "What am I adding here". If the content are generated could be regenerated with simply obvious prompts and there is no knowledge added then this would indicate little added value. 

#### Evolving Societal Rules and Standards

As AIs become ubiquitous and predominant tools, societal attitudes to AI-generated content will change and may become clearer. 

### Strategies for Mitigating Risk

### Testing

Testing outputs of LLMs is important. It reduces risk and ensures that you understand the content output. Testing can take many forms. You might reason through an LLM's outputs, critically assessing each of its assertions using logic or cross-checking against other material. Testing of LLM-generated code might be similar to how you'd test your own code: you could write unit tests or try out the produced application, testing different usage scenarios and checking for errors.  

### Understanding Consequences and Setting a Risk Tolerance

In some cases, you may be able to tolerate some error. For example, if you are learning about trigonometry and you are going to read a wide variety of material, it may be okay if an LLM misleads you, as you will discover this error in further learning or exercises. In other cases, errors could be catastrophic. For example, an LLM may incorrectly analyze a series of medical documents and recommend a dangerous or incorrect treatment plan. Understanding consequences and setting an appropriate risk tolerance when using LLMs is essential.

### Censoring Data

One strategy for using LLMs with sensitive data is to generate mock data, metadata, or data structures that remove any sensitive aspects of the data. This must be approached carefully as, depending on the remaining information content, some data censoring techniques can be reversed. In some cases, it may be safe to provide an LLM with column names and statistical properties of the data in the columns. LLMs can also indirectly assist in censoring data by writing scripts to generate representative datasets. For example, you might ask an LLM to "Generate a python script that reads my CSV and replaces the lat and lon of each location in the location field with random lats and lons". In this example, it would still be necessary to understand how the suggested script worked and whether it was sufficient to censor your data. In many cases, when directly using LLMs, you won't want to send all the data to the LLM. Rather, you may be asking the LLM something about querying or processing your data. In that case, it may be sufficient to send the structure, e.g., the column names, along with a broad description of the data to the LLM.

Sensitive data in other circumstances might include things like file paths, and you could remove these and substitute them with placeholders.  

### Working on Adjacent Problems

Where there is a risk of exposure of intellectual property or sensitive data, it still may be possible to indirectly work with LLMs. For example, you may need to learn and employ a statistical technique on your dataset. It might be possible to learn this technique and work with the LLM to generate code without any specifics of the work you are doing being provided to the LLM. Caution should be taken as over many interactions with an LLM, it may be possible for an adversary to glean information about your IP or data by looking at trends and context.  

> ## Understand Terms and Conditions 
>  
> Find the privacy terms and conditions for OpenAI's ChatGPT. 
> 
> {: .text}
{: .challenge}

> ## Trick an LLM 
>  
> Try to find a mistake in an LLM by asking a really tricky question at the edge of your domain knowledge.
> 
> {: .text}
{: .challenge}

> ## Examples of Sensitive Data
>  
> Think of some examples of sensitive code in your context. 
> 
> {: .text}
{: .challenge}

> ## Safe Interactions
>
> Can you think of any safe ways of engaging an LLM around your problem when there may be a sensitive aspect?
> 
> {: .text}
{: .challenge}

> ## Testing Results
>
> How could you test LLM output in your context?
> 
> {: .text}
{: .challenge}

### Note
GPT-4 was used to rewrite drafts of this material and made minor contributions to the content
