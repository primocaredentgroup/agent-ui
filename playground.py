
from agno import Agent, Team
from agno.agent_ui import AgentUI
from agents.team import build_fun_team
from dotenv import load_dotenv
import os

load_dotenv()

# Costruisci il team
team = build_fun_team()

# Lancia la UI
AgentUI(team).run()
