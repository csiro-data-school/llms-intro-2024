---
title: "What are LLMs and Generative AI"
teaching: 20
exercises: 40
questions:
- "How does an LLM differ from other ML?"
- "What other kinds of Generative AI are there?"
objectives:
- "Introduce LLM and Generative AI"
keypoints:
- "LLMs are Large Language Models; they are specialized ML models that interpret natural language and generate appropriate text responses."
- "Other kinds of Generative AI include Image and Audio generation models."
---

## LLMs and Generative AI

LLMs are Large Language Models, a type of trained ML model. The most famous LLM is ChatGPT. A simple way to consider LLMs is as an AI conversational partner.

LLMs interpret and generate text; they are very good at generating appropriate responses to input text. As a result, they are highly capable of answering questions, creative writing, human-like small talk, and text analysis.

Furthermore, because they have been trained on vast amounts of existing text, they are capable of many tasks beyond what we considered traditional human-like capabilities.

LLMs, especially those comparable to ChatGPT-4:

1. Have vast knowledge and can generally respond accurately to a wide variety of questions.
2. Adapt answers creatively, for example, responding with factual answers as poetry or pretending to be a character.
3. Write fairly competent computer code in a wide variety of languages.
4. Display creativity and can generate unique ideas.
5. Can analyze large amounts of input text or data.

A key in learning how to use LLMs effectively is to experiment. Try different inputs. Think of what tasks an LLM could help with. Explore trying to use an LLM for *all* tasks associated with a broad task or goal. Use an LLM instead of Google, is it reliable and useful? Try comic exchanges with an LLM or asking it to produce creative outputs.

> ## LLM training
> Large Language Models are trained on very large amounts of text (sometimes called the training corpus). Training involves different techniques, but a predominant technique is to complete bits of text correctly. For example, during training, models will be scored more highly if they often complete the fragment "The sky is" with words like "blue," "cloudless," or "cloudy," etc. One of the amazing things about ML techniques, including the training of LLMs, is that when the model gets an incorrect answer, there is normally a mathematical approach to discovering which way to adjust the model parameters to get closer to a correct answer. This makes training ML models much more efficient than a random search for model parameters. According to ChatGPT-4: GPT-4 level LLMs are trained on approximately 1 trillion words. Humans consume around 0.073% of that during their entire lifetimes.
{: .callout}

> ## LLM philosophically
> There has been significant debate about the creative abilities of LLMs. Research shows that when humans use LLMs, their task performance improves. [Source](https://www.science.org/doi/full/10.1126/science.adh2586). LLMs are not simply "likely word generators" or "statisitical parrots". Rather evidence is accumulating that LLMs have "world models" that is the ability to represent aspects or mechanics of the world as systems and rules widely applicable to predict future states. For example it's been found that a GPT trained on the board game Othello appears to represent the state of the board internally [Source](https://thegradient.pub/othello/).   
> 
> With some experience using LLMs they may give appear very useful giving the strong impression that they perform at levels supassing humans on many useful tasks. As LLMs and Generative AI continue to be developed it is likely that their capacity for amazing feats will continue to improve and speculation will shift away from whether these agents are truly intelligent or creative towards a more nuanced discussion of how they work.  
{: .callout}

### Examples of interactions with ChatGPT-4

1. Historical knowledge

> Can you give me a short biography of Pliny the Elder?
> ChatGPT
> Certainly! Here is a short biography of Pliny the Elder:
> Pliny the Elder (Gaius Plinius Secundus) was a Roman author, naturalist, and natural philosopher, as well as a naval and army commander of the early Roman Empire. He was born in 23 AD in Como, Italy, and died on August 25, 79 AD, during the eruption of Mount Vesuvius, which also destroyed Pompeii and Herculaneum.
> ...

2. Adapting answers creatively

> Explain it as if for a 5-year-old
> ChatGPT
> Sure!
>
> Pliny the Elder was a man who lived a long time ago, almost 2,000 years ago, in a place called Rome. He loved to learn about everything around him, like animals, plants, stars, and rocks. He wrote a very big book about all these things so people could learn from him.
> He was also a brave soldier and sailor who traveled to many places. One day, a big volcano called Mount Vesuvius erupted, and Pliny went to help his friends who were in danger. Sadly, he didn't make it, but people remember him because of all the wonderful things he wrote about the world.

3. Writing fairly competent computer code in a wide variety of languages

> Write a very short amusing Python one-liner
> ChatGPT
>
> Here's an amusing Python one-liner that prints "Hello, World!" in a creative way:
>
> ```python
> print("".join(["H", "e", "l", "l", "o", ", ", "W", "o", "r", "l", "d", "!"]))
> ```

4. Displaying creativity and generating unique ideas

> [previous conversation after asking it for ideas for new kids' games]
> Simpler, easy for kids to do but still different from previous games
> ChatGPT
> Rainbow Relay
>
> Objective: A relay race where teams collect colored items to complete a rainbow.
>
> How to Play:
>
> Setup:
> Divide the play area into two sections: a starting line and a collection area where colored items are scattered.
> Items can be anything small and easy to carry, like colored bean bags, balls, or even paper cutouts.

5. Analyzing large amounts of input text or data

> ```
> {
>     "_id": "665176f7ff5d104604d83b42",
>     "index": 0,
>     "guid": "cc81e173-a172-4ae8-b855-567a6c8a9100",
>     "isActive": true,
>     "balance": "$2,355.43",
>     "picture": "http://placehold.it/32x32",
>     "age": 37,
>     "eyeColor": "blue",
>     "name": "Bridges Shepard",
>     "gender": "male",
>     "company": "IMKAN",
>     "email": "bridgesshepard@imkan.com",
>     "phone": "+1 (877) 533-3960",
>     "address": "249 Little Street, Wikieup, Maine, 3400",
>     "about": "Eiusmod magna reprehenderit exercitation Lorem ut mollit eiusmod consequat irure. Amet cillum dolore Lorem non consequat aute eiusmod esse anim. Et consequat non tempor incididunt mollit dolore consequat quis adipisicing do irure exercitation cupidatat.\r\n",
>     "registered": "2020-07-06T06:36:11 -10:00",
>     "latitude": 15.778663,
>     "longitude": -42.518878,
>     "tags": [
>       "pariatur",
>       "quis",
>       "veniam",
>       "eiusmod",
>       "consequat",
>       "incididunt"
>     ],
>     "friends": [
>       {
>         "id": 0,
>         "name": "Baldwin Walker"
>       },
>       {
>         "id": 1,
>         "name": "Katharine Santana"
>       },
>       {
>         "id": 2,
>         "name": "Robinson Lopez"
>       }
>     ],
>     "greeting": "Hello, Bridges Shepard! You have 7 unread messages.",
>     "favoriteFruit": "apple"
> }
> ```

> What might this record mean?
> ChatGPT
> This record represents a person's profile or a user account. Here are the key details:
>
> - `_id`: Unique identifier for the record.
> - `index`: Index position in the database.
> - `guid`: Globally unique identifier.
> - `isActive`: Indicates whether the account is active.
> - `balance`: Account balance.
> - `picture`: URL to the profile picture.
> - `age`: Age of the person.
> - `eyeColor`: Eye color.
> - `name`: Name of the person.
> - `gender`: Gender.
> - `company`: Company name.
> - `email`: Email address.
> - `phone`: Phone number.
> - `address`: Address.
> - `about`: A brief description or summary about the person (though it seems like placeholder text).
> - `registered`: Date and time the person registered or the record was created.
> - `latitude` and `longitude`: Geographical coordinates.
> - `tags`: Keywords associated with the person or the record.
> - `friends`: List of friends associated with the person, each with an `id` and `name`.
> - `greeting`: A personalized greeting message.
> - `favoriteFruit`: Favorite fruit.
>
> This record might be part of a database for a company or service that includes personal, contact, and additional information about its users or clients. The tags and placeholder text in the "about" section suggest it might be a demo or sample record used for testing purposes.

> ## Explore Creativity with LLMs
>
> Think of a task an unpleasant task like doing the dishes and ask an LLM to help suggest creative ways of fixing it. Continue to prompt the LLM asking for strange and unreasonable (but not unsafe) variations on its responses. Comment on the responses' structure.
>
> {: .text}
{: .challenge}

> ## Learn a new skill with LLMs
>
> Ask about a technique familiar to you in your scientific field, get the LLM to suggest new techniques that you may not have used. Comment on the suitability of the techniques. Follow up with questions on specific aspects.
>
> {: .text}
{: .challenge}

> ## Analyze some data
>
> Paste the data from here https://world.openfoodfacts.org/api/v0/product/5060292302201.json into an LLM and ask it what it is. Ask for further details.
>
> {: .text}
{: .challenge}

> ## Write some Code
>
> Write code using an LLM to generate Python code that implements a basic example of Conway's Game of Life. Try executing it in the JupyterLab.
>
> {: .text}
{: .challenge}

---

### Note
GPT-4 was used to rewrite drafts of this material and made minor contributions to the content
