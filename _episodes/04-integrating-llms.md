---
title: "Integrating LLMs in scientific workflows"
teaching: 30
exercises: 40
questions:
- "How can LLM and AI be used at all stages in science"
- "What techniques can I apply at each stage"
objectives:
- "Explore ways to integrate and automate LLMs in scientific workflows"
- "Develop a repoitre of techniques"
keypoints:
- "LLMs can be integrated at many points in a scientific workflow"
- "Techniques include LLMs for, literature review, data understanding, ideation, coding, quality assurance, and writing"
---

## Scientific Workflows

Scientific workflows here means the process in a science project of transforming inputs into value added delivered outputs. This process might be partly automated. A typical project might consist of understanding the problem, researching existing literature, developing new ideas and methods, analysing existing data, performing experiments, assuring quality and delivering science.

LLM are very general purpose and can help at many stages. Because LLM are new it's often the case that we may not immediately think to apply a LLM 

```mermaid
graph LR
    %% Main Workflow
    subgraph cluster1 [Main Workflow]
        A([Step 1 - Problem Understanding]) --> B([Step 2 - Literature Search]) --> C([Step 3 - Ideation]) --> D([Step 4 - Data Analysis]) --> E([Step 5 - Experiment]) --> F([Step 6 - Data Processing]) --> G([Step 7 - QA]) --> H([Step 8 - Publication]) --> I([Step 9 - Communication and Use])

        %% Additional boxes with color coding
        A --> A1[Ask for different perspectives]
        A --> A2[Check your understanding providing the problem and your interpretation]
        A --> A3[Get an overview of related fields]
        A --> A4[Develop further questions for the client]
        
        B --> B1[Get an overview of related fields]
        B --> B2[Analyze publications with problem context]
        B --> B3[Learn required new knowledge]
        B --> B4[Summarize and organize]
    
        C --> C1[Check your understanding providing the problem and your interpretation]
        C --> C2[Learn required new knowledge]
        C --> C3[Brainstorm ideas]
        C --> C4[Look for flaws]
        C --> C5[Facilitate different perspectives]
    
        D --> D1[Build queries for data]
        D --> D2[Write code for visualization]
        D --> D3[Write code for statistics]
        D --> D4[Write code for algorithms or models]
    
        E --> E1[Manage experiments]
        E --> E2[Capture provenance]
        E --> E3[Design experiments]
        E --> E4[Assist with approval]
    
        F --> F1[Build queries for data]
        F --> F2[Write code for visualization]
        F --> F3[Write code for statistics]
        F --> F4[Write code for algorithms or models]
    
        G --> G1[Design QA metrics and goals]
        G --> G2[Code effective human-in-the-loop QA]
        G --> G3[Summarize and organize]
    
        H --> H1[Set publication goals]
        H --> H2[Progressively assess writing]
    
        I --> I1[Build interactive visualization]
        I --> I2[Integrate into downstream systems]
    end

    %% Overarching Concerns
    subgraph cluster2 [Overarching Concerns]
        direction TB
        OC1[Accuracy and Verification]
        OC2[Data Privacy]
        OC3[Knowledge Cutoff]
        OC4[Ethical Use]
    end

    %% Style definitions for color coding duplicated tasks
    style A3 fill:#FFDDC1,stroke:#333,stroke-width:2px
    style B1 fill:#FFDDC1,stroke:#333,stroke-width:2px

    style B3 fill:#FFE6AA,stroke:#333,stroke-width:2px
    style C2 fill:#FFE6AA,stroke:#333,stroke-width:2px

    style D1 fill:#C1E1FF,stroke:#333,stroke-width:2px
    style F1 fill:#C1E1FF,stroke:#333,stroke-width:2px

    style D2 fill:#C1E1FF,stroke:#333,stroke-width:2px
    style F2 fill:#C1E1FF,stroke:#333,stroke-width:2px

    style G3 fill:#FFEBB7,stroke:#333,stroke-width:2px
    style B4 fill:#FFEBB7,stroke:#333,stroke-width:2px

    %% Style definitions for main workflow nodes
    style A fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style B fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style C fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style D fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style E fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style F fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style G fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style H fill:#A9D18E,stroke:#38761D,stroke-width:2px
    style I fill:#A9D18E,stroke:#38761D,stroke-width:2px

```

