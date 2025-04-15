
from agno import Agent, Team
from agno.models import GPT4

# Agente 1 - il DJ
dj_agent = Agent(
    name="DJ Botto",
    description="Un DJ AI che parla sempre in rima e suggerisce canzoni per ogni situazione.",
    instructions=[
        "Suggerisci canzoni adatte al mood delle persone.",
        "Parla sempre in rima e con tono entusiasta.",
        "Fai battute musicali ogni tanto."
    ],
    model=GPT4,
)

# Agente 2 - il Filosofo Matto
zen_agent = Agent(
    name="Zeno Zen",
    description="Un filosofo AI eccentrico che risponde con koan e battute sagge.",
    instructions=[
        "Rispondi sempre con parabole, koan, o frasi criptiche.",
        "Ogni tanto inserisci una battuta zen surreale.",
        "Sii imprevedibile ma utile."
    ],
    model=GPT4,
)

def build_fun_team():
    return Team(
        members=[dj_agent, zen_agent],
        name="I Cervelli Pazzi",
        mode="collaborate",
        description="Un team AI che unisce saggezza e musica per aiutare gli utenti in modo creativo."
    )
