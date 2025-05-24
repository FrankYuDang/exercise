# game.py 
# import the draw module
# import draw



# def main():
#     result = play_game()
#     draw.draw_game(result)
    
# # this means that if this script is executed, then
# # main() will be executed
# if __name__ == '__main__':
#     main()
    
    

# game.py
# import the draw module
from draw import draw_game


#You may have noticed that in this example, 
# the name of the module does not precede draw_game,
# because we've specified the module name using the import command.
#
def play_game():
    pass 

def main():
    result = play_game()
    draw_game(result)