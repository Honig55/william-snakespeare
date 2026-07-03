#import torch
import helpers.debugger as debugger
import game

dbg = debugger.Debugger(active=True, show_time_stamp=True)

game = game.Game(size=15)

dbg.dbg(game.get_training_score())
dbg.dbg(game.get_score())

dbg.dbg("done!")