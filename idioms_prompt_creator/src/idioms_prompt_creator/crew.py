from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class IdiomsPromptCreatorCrew:
    """IdiomsPromptCreator crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    # agents: List[BaseAgent]
    # tasks: List[Task]

    @agent
    def literal_prompt_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["literal_prompt_generator"], verbose=True
        )

    @agent
    def linguistic_stylist(self) -> Agent:
        return Agent(config=self.agents_config["linguistic_stylist"], verbose=True)

    @agent
    def data_curator(self) -> Agent:
        return Agent(config=self.agents_config["data_curator"], verbose=True)

    @agent
    def linguistic_quality_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["linguistic_quality_evaluator"], verbose=True
        )

    @task
    def prompt_task(self) -> Task:
        return Task(config=self.tasks_config["prompt_task"])

    @task
    def linguistic_task(self) -> Task:
        return Task(config=self.tasks_config["linguistic_task"])

    @task
    def curator_dataset_task(self) -> Task:
        return Task(config=self.tasks_config["curator_dataset_task"])

    @task
    def quality_evaluator_task(self) -> Task:
        return Task(config=self.tasks_config["quality_evaluator_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the PromptProject crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
