## JAAS AI 

JaaS AI is a turnkey evaluationAI service that scores, analyzes, validates and monitors any AI-generated text in seconds. Plug JaaS AI into your workflow to ensure accuracy, consistency, and quality—without needing extra reviewers. The system evaluates responses based on customizable criteria and provides detailed scoring and reasoning.
JaaS AI has been proven to detect Hallucination in AI Agents and chat bots.

*Put your workflows and chat bots under the microscope and understand when they start to derail, hallucinate or degrade their accuracy.*

### Requirements

To configure you n8n node, you need a JaaS API key. For that you have to register for the service at jaas-ai.net.You will also need a LLM Provider API key.


### Understanding the evaluation process

The evaluation process is very simple. It compares an *answer* to a specific *question* to a *ground truth answer* in a *context* given. A *score* and *reasoning* is provided based on a *criteria* or criterion given to evaluate.

#### Inputs to the evaluation
- . **question:** The question that you want to evaluate. Example: *Which is capital of France?*

- . **answer:** This is the answer that is going to be evaluated. Example: *Paris*.

- . **ground_truth_answer**: This is the source of truth. It is used as rubric to for the evaluation process to score the criterion. Example: *The capital of France is Paris.*

- . **context:** Additional information that is used to evaluate. The context becomes more relevant in non-direct comparison criterion. As an example in cases of **hallucination:** The context is key to understand if the evaluated answer related to the conversation that has been happening. Example: *Paris is the capital and largest city of France, with an estimated population of 2,048,472 in January 2025 in an area of more than 105 km2 (41 sq mi).*

- . **criteria:** The criteria or criterion is the base of the scoring process. The evaluation tool scores the *answer* based on the criteria given. Example: *Accuracy, Hallucination.*

- . **type:** This is the type of evaluation. There are 4 types: *Simple (S), Conversational Simple (D),
  -  The main differences are: *conversational or non-conversations*: the *conversational* types detect chit-chat conversations that are not evaluated. This is key when evaluating or monitoring *chat bots* or transcripts of *voice conversations*.  

- . **cohort:** The *cohort* helps in the monitoring and analysis process. It does not intervene in the evaluation itself, while indicates a grouping of evaluation. As an example, if the tool is evaluating conversations from a chat bot, each conversation can have its own cohort for better tracking and monitoring.


#### Example of a Information for an evaluation
```json

From Input to the Node:	
  "question": "What is the capital of France?",
  "answer": "Paris.",
  "ground_truth_answer": "Paris is the capital of France.",
  "context": "",

From Configuration:
	"evaluation_criteria": ["Accuracy", "Hallucination"],
  "type": "S",
  "cohort":"ChatBot1"

```
After the evaluation is completed almost in real time, the system returns the score for each of the metrics and the reasoning behind.


### Using the n8n JaaS Module

***Configuration:*** The module requires the corresponding configuration:
	- JaaS API Key: linked to you account in jaas-ai.com
	- Criteria: you can enter up to 3 criteria for each node. The criteria should be available in teh Criteria Database in jaas-ai.com.
	- Type of Evaluation: S - Simple, or C- Conversational
	- Cohort: to groupe the evaluations in groups for better tracking
  
***Input:*** You should provide the no de the fields needed for the evaluation:
	- question: question to answer
	- answer: answer that has to be evaluated
	- ground_truth_answer: source of truth for the answer to be evaluated
	- context: additional information to help the evaluation process
The inputs should be in Json Format.

Obtain the results and monitor what is going on with your tools!

Look for more information and examples in our website!!

support: support@jaas-ai.com
website: jaas-ai.net
