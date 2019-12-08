import argparse
import yaml
import sys
import os

class Parser():


    def setup_parser(self):
        parser = argparse.ArgumentParser(description="A CLI tool to make deployment of airflow projects faster")
        #parser.add_argument("-v", "--version", action="store_true")  #learn the standard way to add version to python package
        new_parser = parser.add_subparsers()
        sub_parser = new_parser.add_parser("init", help="Create a boilerplate code for your airflow project")
        sub_parser.set_defaults(func=self.create_project)
        sub_parser.add_argument("-n", "--name", help="Name of your airflow project", required=True)
        sub_parser.add_argument("-p", "--plugin", help="Add plugin to your project", choices=self.plugins, required=True)
        sub_parser = new_parser.add_parser("list", help="Get list of operators, sensors, plugins, hooks.")
        sub_parser.set_defaults(func=self.list)
        sub_parser.add_argument("type", choices=self.choices)
        parser.add_argument("--easter_egg")
        parser.set_defaults(func=self.easter)
        return parser

    def create_project(self, args):
        pass

    def list(self, args):
        print("Available {} :".format(args.type))
        vals = eval("self.{}".format(args.type))
        print('\n'.join(map(str, vals)))

    def __init__(self):
        try:
            with open("{}/{}".format(os.path.dirname(os.path.abspath(__file__)), 'meta.yml')) as file:
                self.data = yaml.full_load(file)

            self.choices = [k for k in self.data]
            self.operators = self.data['operators'].split(' ')
            self.hooks = self.data['hooks'].split(' ')
            self.sensors = self.data['sensors'].split(' ')
            self.plugins = self.data['plugins'].split(' ')
        except:
            sys.exit(3)

    def easter(self, args):
        if vars(args)['easter_egg'] == "I love open source.":
            print("""
              __  __           _                 _ _   _       _                     
             |  \/  |         | |               (_) | | |     | |                    
             | \  / | __ _  __| | ___  __      ___| |_| |__   | |     _____   _____  
             | |\/| |/ _` |/ _` |/ _ \ \ \ /\ / / | __| '_ \  | |    / _ \ \ / / _ \ 
             | |  | | (_| | (_| |  __/  \ V  V /| | |_| | | | | |___| (_) \ V /  __/ 
             |_|  |_|\__,_|\__,_|\___|   \_/\_/ |_|\__|_| |_| |______\___/ \_/ \___| 
              ____           ____        _           _                               
             |  _ \         / __ \      | |         | |                              
             | |_) |_   _  | |  | |_   _| |__   ___ | | ___                          
             |  _ <| | | | | |  | | | | | '_ \ / _ \| |/ _ \                         
             | |_) | |_| | | |__| | |_| | |_) | (_) | |  __/                         
             |____/ \__, |  \___\_\\__,_|_.__/ \___/|_|\___|                         
                     __/ |                                                           
                    |___/                                                  
                    """)
        else:
            print("Try again :p")
