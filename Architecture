# Software Structure and plan

## Architecture


|----------------|      |----------------|        |----------------|
|                |      |                |        |                |
|    **Model**   | ====>|  **Software**  | =====> |  **UI & API**  |
|                |      |                |        |                |
|----------------|      |----------------|        |----------------|


## Model
This is a fine-tuned Large Language model (definitely an Auto-encoder model i.e Encoder-Only LLM since they most effective in Name Entity Recognition). This model will recieve text prompts (later versions will have voice reception capabilities) with the aim of returning 4 fundamental outputs:
1. Action : is it a schedule or reschedule
2. Message: What action is to be performed
3. Timing: When is it to be executed with respect to now
4. Recurrence: Is this task repitive? if so how often? or is it a one-time activity.

These actions will be processed into a format most useful to the Software that manages the scheduling and rescheduling. The intelligent part of the project ends here. The goal of the intelligence is to ensure that it understands what the user is communicating and return it to the software. Also this section of the platform will be useful in enhancing the user experience because it is the interface between the entire software and the user, so it will be conversational. That is the utility of the LLM: the user experience.

## Software
It is the less fancy part of the software but essentially the heart. It get's it's input from the model and executes on the database of the user. Based on information logged, every prompt is to be examined and executed error free, then feedback on Execution is passed to the model for processing and output to the user. Based on the outcome from execution, the software block will send information to the model on the success status. The model will then communicate with the user via the interface at work (API or Direct User interface).

## UI & API
This is the integration face.
This product is intended to have a web interface, a mobile phone interface and cloud based service that is integratable to smart IoT devices. It can live in a Raspberry Pi computer and hopefully live in a fully  independent hardware product. Also the API would be to integrate it in existing calendar systems or for other developers to build more software on it.
Nonetheless, Reawired is focused on its web outlet for initial versions. **The future is pregnant!**
