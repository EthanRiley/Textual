from Textual import textual

def main():
    tt = textual()
    drake_songs = ['CombinedCode/Drake/cant_take_a_joke.txt', 'CombinedCode/Drake/dont_matter_to_me.txt', 
                'CombinedCode/Drake/nine.txt', 'CombinedCode/Drake/nonstop.txt', 
                'CombinedCode/Drake/redemption.txt', 'CombinedCode/Drake/views.txt']
    drake_text = textual.combine_txt(drake_songs)
    kanye_songs = ['CombinedCode/Kanye/all_falls_down.txt', 'CombinedCode/Kanye/jesus_walks.txt', 
                'CombinedCode/Kanye/dark_fantasy.txt', 'CombinedCode/Kanye/never_let_me_down.txt', 
                'CombinedCode/Kanye/power.txt', 'CombinedCode/Kanye/runaway.txt']
    kanye_text = textual.combine_txt(kanye_songs)
    kendrick_songs = ['CombinedCode/Kendrick/alright.txt', 'CombinedCode/Kendrick/blacker_the_berry.txt', 
                'CombinedCode/Kendrick/dont_kill_my_vibe.txt', 'CombinedCode/Kendrick/king_kunta.txt', 
                'CombinedCode/Kendrick/maad_city.txt', 'CombinedCode/Kendrick/money_trees.txt']
    kendrick_text = textual.combine_txt(kendrick_songs)
    tt.load_text(drake_text, 'Drake')
    tt.load_text(kanye_text, 'Kanye')
    tt.load_text(kendrick_text, 'Kendrick')
    tt.word_count_sankey(title='Rappers1')
    tt.word_count_sankey(title='RappersWordList', word_list=['yeah', 'no', 'like'])


main()
    
