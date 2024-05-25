---
title: "What are LLMs and Generative AI"
teaching: 20
exercises: 40
questions:
- "How does an LLM differ from other ML?"
- "What other kinds of Generative AI is there?"
objectives:
- "Introduce LLM and Generative AI"
keypoints:
- "LLMs are Large Language Models they are specialised ML models that interpret natural language and appropriate text responses"
- "Other kinds of Generative AI includes Image and Audio generation models"
---

## LLMs and Generative AI

LLMs are Large Lanaguge Models they are a type of trained ML model. The most famous LLM is ChatGPT. A simple way to consider LLMs is as an AI conversational partner.  

LLMs interpret and generate text they are very good at generating appropriate responses to input text. As a result they are highly capable of answering questions, creative writing, human like small talk, and analysis of text.  

Furthermore becuase they have been trained on very vast amounts of existing text they are capable of many tasks that are beyond what we considered to be traditional human like capabilities. 

LLMs especially those comparable to ChatGPT 4: 

1. Have a vast knowledge and can * generally * respond accurately to a wide variety of questions. 
2. Adapt answers creatively, for example responding with factual answers as poetry or pretending to be a character
3. Write farily compentent computer code in a wide variety of languages
4. Display creativity and can generate some unique ideas
5. Can analyze large amounts of input text or data

### Examples of interactions with ChatGPT 4

1. Historical knowledge

> Can you give me a short biography of pliny the elder?  
> ChatGPT  
> Certainly! Here is a short biography of Pliny the Elder:  
> Pliny the Elder (Gaius Plinius Secundus) was a Roman author, naturalist, and natural philosopher, as well as a naval and army commander of the early Roman Empire. He was born in 23 AD in Como, Italy, and died on August 25, 79 AD, during the eruption of > Mount Vesuvius, which also destroyed Pompeii and Herculaneum.  
> ...

2. Adapting answers creatively


> Explain it as if for a 5 year old  
> ChatGPT  
> Sure!  
>   
> Pliny the Elder was a man who lived a long time ago, almost 2,000 years ago, in a place called Rome. He loved to learn about everything around him, like animals, plants, stars, and rocks. He wrote a very big book about all these things so people could learn from him.  
> He was also a brave soldier and sailor who traveled to many places. One day, a big volcano called Mount Vesuvius erupted, and Pliny went to help his friends who were in danger. Sadly, he didn't make it, but people remember him because of all the wonderful things he wrote about the world. 

3. Write farily compentent computer code in a wide variety of languages

> Write a very short amusing python one liner  
> ChatGPT  
>   
> Here's an amusing Python one-liner that prints "Hello, World!" in a creative way:  
>   
> python  
>   
> print("".join(["H", "e", "l", "l", "o", ", ", "W", "o", "r", "l", "d", "!"]))  
>   
> This one-liner constructs the string "Hello, World!" by joining individual characters in a list.  

4. Display creativity and can generate some unique ideas

> [previous conversation after asking it for ideas for new kids games]
> ...  
> Simpler easy for kids to do but still different to previous games  
> ChatGPT  
> Rainbow Relay  
>  
> Objective: A relay race where teams collect colored items to complete a rainbow.  
>  
> How to Play:  
>  
>    Setup:  
>        Divide the play area into two sections: a starting line and a collection area where colored items are scattered.
>        Items can be anything small and easy to carry, like colored bean bags, balls, or even paper cutouts.

5. Can analyze large amounts of input text or data

> [  
>   {  
>     "_id": "665176f7ff5d104604d83b42",  
>     "index": 0,  
>     "guid": "cc81e173-a172-4ae8-b855-567a6c8a9100",  
>     "isActive": true,  
>     "balance": "$2,355.43",  
>     "picture": "http://placehold.it/32x32",  
> ...  
>     "email": "bridgesshepard@imkan.com",  
>     "phone": "+1 (877) 533-3960",  
>     "address": "249 Little Street, Wikieup, Maine, 3400",  
>     "about": "Eiusmod magna reprehenderit exercitation Lorem ut mollit eiusmod consequat irure. Amet cillum dolore Lorem non consequat aute eiusmod esse anim. Et consequat non tempor incididunt mollit dolore consequat quis adipisicing do irure exercitation cupidatat.\r\n",  
> ...  
>   
> What might this record mean?  
> ChatGPT  
> ...  
>     Additional Information:  
>         About: A brief description or summary about the person (though it seems like a placeholder or example text).  
>         Registered Date: 2020-07-06T06:36:11 -10:00 (the date and time the person registered or the record was created)  
>         Geographical Coordinates: Latitude 15.778663, Longitude -42.518878  
>   
>  Tags: Keywords associated with the person or the record, such as "pariatur," "quis," "veniam," "eiusmod," "consequat," and "incididunt."  
>   
> This record might be part of a database for a company or service that includes personal, contact, and additional information about its users or clients. The tags and placeholder text in the "about" section suggest it might be a demo or sample record used for testing purposes.  

> ## Explore Creativity with LLMs 
>  
> Think of a task you dislike doing and ask an LLM to help suggest creative ways of fixing it. Continue to prompt the LLM asking for strange and unreasonable (but not unsafe) variations on it's responses. Comment on the responses structure.
> 
> {: .text}
{: .challenge}


> ## Learn a new skill with LLMs 
>  
> In your existing scientific field ask about a technique you use and get the LLM to suggest new techniques that you may not have used. Comment on the suitability of the techniques. Follow up with questions on specific aspects.
> 
> {: .text}
{: .challenge}


> ## Analyze some data
>  
> Paste the data from here https://world.openfoodfacts.org/api/v0/product/5060292302201.json into an LLM and ask it what it is. Ask for further details
> 
> {: .text}
{: .challenge}

> ## Write some Code
>  
> Write code using an LLM to generate python code that implements a basic example of conways game of life. Try executing it in the jupyterlab.
> 
> {: .text}
{: .challenge}