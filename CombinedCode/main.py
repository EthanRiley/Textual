from Textual import textual

def main():
    drake_songs = ['Drake/cant_take_a_joke.txt', 'Drake/dont_matter_to_me.txt', 
                'Drake/nine.txt', 'Drake/nonstop.txt', 
                'Drake/redemption.txt', 'Drake/views.txt']
    drake_text = textual.combine_txt(drake_songs)


    kanye_songs = ['Kanye/all_falls_down.txt', 'Kanye/jesus_walks.txt', 
                'Kanye/dark_fantasy.txt', 'Kanye/never_let_me_down.txt', 
                'Kanye/power.txt', 'Kanye/runaway.txt']
    kanye_text = textual.combine_txt(kanye_songs)
    kendrick_songs = ['Kendrick/alright.txt', 'Kendrick/blacker_the_berry.txt', 
                'Kendrick/dont_kill_my_vibe.txt', 'Kendrick/king_kunta.txt', 
                'Kendrick/maad_city.txt', 'Kendrick/money_trees.txt']
    kendrick_text = textual.combine_txt(kendrick_songs)
    
