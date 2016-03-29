#!/usr/bin/env python3
from crosses import UI, Board, CliPlayer, AIPlayer

# Run it
ui = UI(Board(), CliPlayer(), AIPlayer())
ui.run()
