7. Adding Cookiecutter for new Event Bus events and their kafka setup
#####################################################################

Status
******

Proposed


Context
*******

Adding new events to the Openedx Event Bus has taken a lot of time and effort in the past.
Specifically, setting up local development with Kafka and connecting it correctly to the new provider,
consumer, and topic has been a challenge.
We want to make this process easier by creating a Cookiecutter template that can be used to
quickly scaffold the necessary files and configurations for a new Event Bus event.

This approach involves not creating one new project directory, but instead code that can be copied
into multiple existing repositories.


Decision
********

* We will add a new folder `cookiecutter-event-bus-kafka-event` to the edx-cookiecutters repository.

* This folder will contain subfolders for each of the following:
  - `openedx-events`: Contains the Open edX event definitions to be copied to the `openedx-events` repository.
  - `provider`: Contains the code for the new provider, as well as any necessary configuration files and environment
    variables needed to connect to the Kafka Event Bus, to be copied to the repository the new provider will be created in.
  - `consumer`: Contains the code for the new consumer, as well as any necessary configuration files and environment
    variables needed to connect to the Kafka Event Bus, to be copied to the repository the new consumer will be created in.
    Also includes a docker-compose file to run the consumer locally.

* Where needed, in the future we should add similar cookiecutter templates for the other Event Bus implementations,
  such as redis, rather than making duplicate work necessary every time a new event is added.

* We will add well-visible central documentation to Confluence to make it easy to find and use this cookiecutter template.


Rejected Alternatives
*********************

Keep template private
=====================================================

Since the Kafka implementation of the EventBus is part of Openedx, we should also make the cookiecutter template available to the Open edX community.

Supporting other Event Bus implementations
=====================================================

Creating templates for multiple Event Bus implementations, including redis, is desirable in the future,
but the immediate need is for the Kafka implementation. Doing the same for redis will need a new large effort.
Currently, the config needed for Kafka has been surfaced by 2U discovery (Quokkas team), providing the knowledge
needed to create the Kafka implementation template.
