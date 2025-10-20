"""
Three-agent academic mentorship workflow using LangGraph (StateGraph) and LangChain's ChatOpenAI.

Flow (strictly sequential): Mentor (scope) -> Analyst (quant) -> Coach (resources) -> Mentor (final synthesis)

All LLM calls use OpenAI via ChatOpenAI and rely on OPENAI_API_KEY.
"""

import os
import argparse
from typing import TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END


class GraphState(TypedDict):
    """Centralized state passed between all nodes."""

    user_input: str
    research_scope: str
    analyst_report: str
    resource_map: str
    final_report: str


def build_llm(model_name: str = "gpt-4o-mini", temperature: float = 0.0) -> ChatOpenAI:
    """Create a ChatOpenAI instance using only the OPENAI_API_KEY environment variable."""
    # ChatOpenAI reads OPENAI_API_KEY from environment.
    # Model choice kept stable per instructions.
    return ChatOpenAI(model=model_name, temperature=temperature)


def node_mentor_scope(state: GraphState) -> dict:
    """Scoping Agent: Refines broad topic into clear research scope.

    Writes: research_scope
    """
    llm = build_llm()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "As a Scoping Agent, create a clear research scope. Keep answers concise and use simple language.\n\n"
                "Provide:\n"
                "1. **Research Question:** One focused question for a semester project\n"
                "2. **Objectives:** 3-4 clear goals\n"
                "3. **Scope:** What you will and won't cover\n"
                "4. **Expected Results:** What you'll deliver\n"
                "5. **Why Important:** Brief relevance explanation\n\n"
                "Keep each section short and clear.",
            ),
            (
                "human",
                "Topic: \"{user_input}\"\n\n"
                "Create a research scope:",
            ),
        ]
    )
    chain = prompt | llm
    result = chain.invoke({"user_input": state["user_input"]})
    content = result.content if hasattr(result, "content") else str(result)
    return {"research_scope": content.strip()}


def node_analyst_quant(state: GraphState) -> dict:
    """Analyst Agent: Provides methodology, metrics, and risk assessment.

    Writes: analyst_report
    """
    llm = build_llm()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "As an Analyst Agent, provide a clear analysis. Keep it concise and simple.\n\n"
                "Provide:\n"
                "1. **Methods:** How you'll approach the research\n"
                "2. **Key Metrics:** 2-3 measurable goals with target values\n"
                "3. **Benchmarks:** Baseline (minimum) and stretch (ambitious) goals\n"
                "4. **Risks:** 3-4 main challenges and how to handle them\n\n"
                "Keep each section brief and practical.",
            ),
            (
                "human",
                "Research: \"{research_scope}\"\n\n"
                "Create an analyst report:",
            ),
        ]
    )
    chain = prompt | llm
    result = chain.invoke(
        {"research_scope": state.get("research_scope", ""), "user_input": state["user_input"]}
    )
    content = result.content if hasattr(result, "content") else str(result)
    return {"analyst_report": content.strip()}


def node_skill_coach(state: GraphState) -> dict:
    """Resource Mapper Agent: Creates learning resources table.

    Writes: resource_map
    """
    llm = build_llm()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "As a Resource Mapper Agent, create a simple learning plan.\n\n"
                "Provide 6-8 essential skills needed for this research.\n"
                "For each skill, give:\n"
                "- Skill name\n"
                "- Specific course/book title\n"
                "- Level: Beginner, Intermediate, or Advanced\n"
                "- Why it's important (one short sentence)\n\n"
                "Format as a simple list, not a table. Keep descriptions short.",
            ),
            (
                "human",
                "Research: {research_scope}\n\n"
                "List the essential skills and resources:",
            ),
        ]
    )
    chain = prompt | llm
    result = chain.invoke(
        {
            "research_scope": state.get("research_scope", ""),
            "analyst_report": state.get("analyst_report", ""),
        }
    )
    content = result.content if hasattr(result, "content") else str(result)
    return {"resource_map": content.strip()}


def node_lead_mentor_synthesis(state: GraphState) -> dict:
    """Planner Agent: Creates project roadmap with timeline.

    Writes: final_report
    """
    llm = build_llm()
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "As a Planner Agent, create a simple project plan. Keep it clear and concise.\n\n"
                "Provide:\n"
                "1. **Success Criteria:** What defines success (2-3 clear goals)\n"
                "2. **30-Day Goal:** What to achieve in first month\n"
                "3. **60-Day Goal:** What to achieve in second month\n"
                "4. **90-Day Goal:** What to achieve in third month\n\n"
                "Keep each section short and practical.",
            ),
            (
                "human",
                "Research: {research_scope}\n"
                "Analysis: {analyst_report}\n"
                "Resources: {resource_map}\n\n"
                "Create a project plan:",
            ),
        ]
    )
    chain = prompt | llm
    result = chain.invoke(
        {
            "user_input": state["user_input"],
            "research_scope": state.get("research_scope", ""),
            "analyst_report": state.get("analyst_report", ""),
            "resource_map": state.get("resource_map", ""),
        }
    )
    content = result.content if hasattr(result, "content") else str(result)
    return {"final_report": content.strip()}


def build_graph() -> any:
    """Construct a strict sequential StateGraph with four nodes."""
    graph = StateGraph(GraphState)

    graph.add_node("mentor_scoper", node_mentor_scope)
    graph.add_node("data_analyst", node_analyst_quant)
    graph.add_node("skill_coach", node_skill_coach)
    graph.add_node("lead_mentor", node_lead_mentor_synthesis)

    graph.set_entry_point("mentor_scoper")
    graph.add_edge("mentor_scoper", "data_analyst")
    graph.add_edge("data_analyst", "skill_coach")
    graph.add_edge("skill_coach", "lead_mentor")
    graph.add_edge("lead_mentor", END)

    return graph.compile()


def run_workflow(user_request: str) -> GraphState:
    """Run the full workflow from Mentor -> Analyst -> Coach -> Mentor and return final state."""
    app = build_graph()
    initial_state: GraphState = {
        "user_input": user_request,
        "research_scope": "",
        "analyst_report": "",
        "resource_map": "",
        "final_report": "",
    }
    final_state: GraphState = app.invoke(initial_state)  # type: ignore
    return final_state


def _print_state(state: GraphState) -> None:
    print("=== Research Scope ===")
    print(state.get("research_scope", ""))
    print()
    print("=== Analyst Report ===")
    print(state.get("analyst_report", ""))
    print()
    print("=== Resource Map ===")
    print(state.get("resource_map", ""))
    print()
    print("=== Final Report ===")
    print(state.get("final_report", ""))


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Please export your OpenAI API key before running."
        )

    parser = argparse.ArgumentParser(
        description=(
            "Run the academic mentorship workflow (Mentor → Analyst → Coach → Mentor) "
            "using LangGraph and OpenAI."
        )
    )
    parser.add_argument(
        "user_input",
        type=str,
        help="Initial request, e.g., 'Analyze this paper and recommend courses'.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="OpenAI model for all nodes (default: gpt-4o-mini)",
    )
    args = parser.parse_args()

    # Allow model override via CLI by temporarily monkey-patching build_llm closure
    # to keep all nodes consistently configured from a single place.
    def _build_llm_override(model_name: str = args.model, temperature: float = 0.0) -> ChatOpenAI:  # type: ignore
        return ChatOpenAI(model=model_name, temperature=temperature)

    global build_llm  # type: ignore
    build_llm = _build_llm_override  # type: ignore

    state = run_workflow(args.user_input)
    _print_state(state)


if __name__ == "__main__":
    main()


