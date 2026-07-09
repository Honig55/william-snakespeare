#import torch
import helpers.debugger as debugger
import battlesnake_objects as game
import agent
import battlesnake_server
import run_local_game

import sys
import yaml


# calling convention:
# python3 myin.py <mode> [<args>]
# currently no args are supported, but this is a placeholder for future expansion

def test(debugger:debugger):
    debugger.dbg("test")

def train():
    # call training
    pass

def run():
    with open("config.yml", "r") as f:
        config = yaml.safe_load(f)
    port = config.get("server_port")

    battlesnake_server.start_server(agent.Agent(), port)
    
    # call server
    pass

if __name__ == '__main__':
    if argv is None or len(argv)<2:
        print("No mode specified, defaulting to local")
        exit(-1)
    
    args = sys.argv[1:]
    
    if len(args) < 1:
        print("No mode specified, defaulting to local")
        exit(-1)

    mode = args[0] if len(args) > 0 else 'local'

    match mode:
        case 'test':
            dbg = debugger.Debugger(active=True, show_time_stamp=True)
            test(dbg)
        case 'train':
            train()
        case 'run':
            run()
        case _:
            print(f"Unknown mode: {mode}")
            exit(-2)