import sys
sys.path.insert(0, ".")
from question1.agent import SupportCopilot

c = SupportCopilot()
c.handle_ticket("T-1001")
for k in c.session.calls:
    print(k.label, "| input:", k.input_tokens, "| cached:", k.cached_prefix_tokens,
          "| output:", k.output_tokens, "| points:", k.points())