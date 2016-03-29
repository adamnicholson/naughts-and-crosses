#!/usr/bin/env python3
from crosses import UI, Board, CliPlayer, AIPlayer

# Run it
ui = UI(Board(), CliPlayer(1), AIPlayer(2))
ui.run()
